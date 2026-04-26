# Java Multi-Repo Primer (for a Django-Brained Reader)
**Session 2, 2026-04-21. Written for Colin.**

Colin's ask: "How does an EPNM application even get run when there are five
repositories for it? I'm a Django guy, I don't even really understand what
a JAR file is." This primer answers that at the level needed to orient
without becoming a Java developer.

Everything below is general Java ecosystem context with inferences pinned
to what the tree reports show. Where a claim about the actual Cisco build
is a guess, it's flagged. The execution session is the authority on how
the Cisco codebase actually builds.

---

## 1. What JARs and WARs are (Django analogies)

**JAR (Java ARchive).** A zip file containing compiled Java class files
(`.class`) plus a manifest. It's the unit a Java library ships as. Think of
it as the rough equivalent of a Python wheel or an npm package — a package
that other Java code can depend on.

**WAR (Web Application ARchive).** A zip file containing a full deployable
web app: JARs, web config (`web.xml`), static resources, templates. It's
what a Java application server (Tomcat, WebLogic, JBoss) takes and hosts.
Equivalent to a Django project that's been packaged for deployment to a
WSGI server — the WAR is the deliverable, the app server is the runtime.

**Uber-JAR / fat JAR.** A JAR with all its dependencies baked in, runnable
directly with `java -jar thing.jar`. This is the Spring Boot shape — it
brings its own embedded Tomcat, and you run the JAR like a self-contained
Python script with `python manage.py runserver`. No external app server
needed.

---

## 2. Why Java projects live across many repos

A large Java application is almost never one repo. Two structural reasons:

1. **Reuse across products.** A framework repo gets shared across many
   applications. In EPNM: the `pf-framework` repo is the Dojo-based UI
   framework, depended on by `assembly` (inventory UI), `fault` (alarms UI),
   `wireless`, and `chassisview`. All of them pull `pf-framework` as a
   dependency. In Django terms, it's a bit like a single reusable
   `django-core-ui` package that every app depends on — just moreso.

2. **Build-time dependency ordering.** Java's compile model has strict
   dependency ordering. Framework repos build first, feature repos build
   second, the deployable repo builds last. Multi-repo makes this ordering
   explicit.

### What the EPNM repo inventory probably means

The seven EPNM repos in the `poc/REPO/` bundle split like this (inference):

| Repo | Probable role in the EPNM build |
|------|---------------------------------|
| `pf-framework` | Core UI framework JAR. Everything else depends on it. |
| `wireless` | Wireless domain framework. Depended on by wireless-specific features. |
| `ce-content-device-packs` | Device-content (CLI templates, MIBs, device-model packs). A data/content JAR consumed at runtime. |
| `assembly` | Inventory and fault UI modules. Builds a WAR or WAR fragment. |
| `inventory` | Inventory backend services (Java). Builds JARs consumed by the deployable. |
| `chassisview` | Chassis visualization component (JS + Java support). JARs + web assets. |
| `fault` | Fault backend + frontend. JARs + web assets. |

The deployable probably isn't any single one of these. It's something assembled
from them — typically a top-level repo that Maven-builds all the others and
produces a WAR or a collection of artifacts for an installer. That top-level
repo is not in the bundle. Whether it exists as a separate repo or as a
branch inside one of these is unknown.

**Inference flag.** The tree reports don't show the top-level assembly
descriptor or installer scripts. The execution session should look for:
- A root `pom.xml` (Maven build descriptor) in each repo.
- A `parent` declaration in `pom.xml` files pointing at a shared root.
- Whether `assembly` or `inventory` or some other repo has a `pom.xml` that
  depends on the others.

---

## 3. How Java builds actually compose

Two dominant Java build tools, Maven and Gradle. Maven is older, XML-based
(`pom.xml`), and overwhelmingly common at large enterprises. Cisco EPNM
almost certainly uses Maven (the tree reports show `pom.xml` everywhere).

Maven concepts Django users care about:

- **POM (`pom.xml`).** The build descriptor for a Java project. Analogous
  to `setup.py` + `pyproject.toml` + part of `requirements.txt` all in one.
- **Groups and artifacts.** Every JAR has a `groupId` (like a namespace —
  `com.cisco.epnm`), an `artifactId` (like a package name — `inventory`),
  and a `version`. Together they identify a JAR uniquely in a repository.
- **Parent POM.** A POM can declare a parent POM. Parents provide shared
  config (common dependencies, common plugin config). EPNM probably has a
  parent POM in its own repo or in one of the existing repos that all the
  rest inherit from.
- **Multi-module Maven project.** A single repo that contains multiple
  sub-modules, each with its own POM, plus a root POM that lists all sub-
  modules. The root `mvn install` walks the sub-modules in dependency
  order, builds each, and installs resulting JARs into the local Maven
  cache (`~/.m2/`). The tree reports show EPNM repos with many sub-
  directories each containing their own `pom.xml` — that's a multi-module
  layout.
- **Dependency resolution.** One project depends on another by declaring
  it in `<dependencies>`. Maven pulls the JAR from the local cache, from
  a configured corporate repository (Cisco has its own Maven repo), or
  from Maven Central. Django's analog is `pip install` against
  `requirements.txt`, with internal PyPI mirrors.

### Rough mental model for EPNM build order

If EPNM follows conventional Maven practice — again, inference — the order
goes roughly:

1. `pf-framework` — core framework. Built first.
2. `wireless` — framework, depends on `pf-framework`.
3. `ce-content-device-packs` — content, may be independent.
4. `chassisview`, `inventory`, `fault`, `assembly` — feature modules.
   Depend on `pf-framework` and (for some) `wireless`.
5. Some top-level assembler — probably elsewhere — combines everything
   into a WAR or installer.

To confirm this: find the `<parent>` block in each repo's root `pom.xml`
and the `<dependencies>` block in a feature repo's POM to see which other
repos it pulls in. The execution session can do this in minutes per repo.

---

## 4. How an EPNM app "runs"

Two radically different runtimes depending on the product:

### EPNM (legacy, Dojo + Java monolith)

Almost certainly runs on an application server (Tomcat, WebLogic, or a
Cisco-internal app-server packaging). The build produces a WAR. The WAR is
deployed to the app server via an installer. The Oracle database is a
separate service. SNMP / CLI collectors are separate processes. Everything
is coordinated through the Cisco installer tooling.

**Local runnability: almost certainly not.** EPNM is designed to be
installed as a product. Running it on a developer laptop without the full
EPNM installer and an Oracle instance is not a supported path. The
execution session can read the code freely but should not expect to
stand it up locally. The EPNM VM (action item A2) is where EPNM actually
runs for observation purposes.

### EMS / CNC (modern, Spring Boot + Go + PostgreSQL)

Spring Boot is the opposite pattern. Each service is a self-contained
runnable JAR. `java -jar cw-inventory.jar --spring.profiles.active=local`
starts one service on a port. You run the services you need, point them
at a local PostgreSQL, and hit them with HTTP requests.

Evidence from the tree-report swarm:
- `cw-inventory` and `cw-inventory-collector` have `LocalProfileConfig`
  classes. That almost always means "when the `local` Spring profile is
  active, use these overridden beans for local development."
- Both repos have `Dockerfile`s. Those build container images of the
  services. For local-run purposes, a `docker-compose.yml` or
  `local-dev.sh` at repo root would show how the service wires to its
  dependencies.
- Angular `unified-ems-ui` is a library, not an app. It has no `ng serve`
  equivalent on its own — it's consumed by `infra-ui`.
- `infra-ui` is an Angular app. `ng serve` (or equivalent through the
  custom webpack config) should work if backend endpoints are reachable.

**Local runnability: plausible but unconfirmed.** The execution session
should verify before any assumption is made. Open question 3.8 captures
the specific investigation steps.

---

## 5. What "the classic view code builds as part of EMS" probably means

Akhil's constraint from the walkthrough: "It has to be part of the new EMS
build." Given the EMS build shape:

- If classic-view code lives as a subfolder of `unified-ems-ui`'s
  `ems-lib/src/app/`, it's built as part of the library. The library is
  packaged, the shell consumes it, the whole thing deploys. Clean.
- If classic-view code lives as a new standalone repo, that repo must
  either be a new Angular library that `unified-ems-ui` or `infra-ui`
  consumes, or a new Angular app that replaces the EMS feature layer.
  More coordination; not the natural shape.

The tree-report evidence favors a subfolder of `unified-ems-ui`'s
`ems-lib` (with a coordinated mount point added in `infra-ui`'s routes
and module list). That's a proposal for Colin to own — Akhil asked him
for it.

---

## 6. What to do when confused by a Java project

A practical workflow for a Django-brained engineer dropped into a Java
multi-repo world:

1. Find every `pom.xml` at each repo's root. Read the `<parent>`,
   `<artifactId>`, `<dependencies>` sections. Stop when you can draw a
   dependency graph.
2. Find the build-and-package script. In Maven, it's usually
   `mvn clean package` at the root. In Cisco internal, it may be a
   wrapper script.
3. Find the runtime entry. For Spring Boot, it's a class annotated with
   `@SpringBootApplication`. For a WAR, it's `web.xml` + `web-fragment.xml`.
4. Look for `application.yml`, `application.properties`, or
   `bootstrap.yml`. These are Spring Boot's Django `settings.py`.
5. Look for a README or a `docs/` folder at each repo root.

None of this is actual code writing. It's ten minutes of orientation that
tells you how the thing is meant to run.

---

## 7. Bottom line for the EPNM-EMS POC

- EPNM is a legacy monolith packaged for installer-based deployment. Read
  it, don't try to run it locally. Use the EPNM VM for observation once
  provisioned.
- EMS is a modern Spring Boot + Angular stack. Each backend service is
  in principle a self-contained runnable JAR. Local-run of the frontend
  shell is plausible; local-run of the backend is plausible; end-to-end
  local is an open question (3.8). The execution session investigates.
- The classic-view code most naturally lives inside the `unified-ems-ui`
  Angular library as a subfolder, with a coordinated mount in `infra-ui`'s
  navigation and routes.

---

## 8. Glossary

- **JAR** — Java archive. A compiled Java library.
- **WAR** — Web application archive. A deployable Java web app.
- **Maven** — Java build tool. XML build descriptors (`pom.xml`).
- **POM** — `pom.xml`, the Maven build descriptor.
- **Spring Boot** — Java web framework. Produces self-contained runnable
  JARs with embedded Tomcat. The "modern" Java shape.
- **Dojo 1.x** — Legacy JavaScript framework used by EPNM's UI.
- **Tomcat / WebLogic / JBoss** — Java application servers. EPNM likely
  runs on one of these.
- **ADS** — Cisco internal application deployment infrastructure (inferred
  from Saurav transcript context). Likely where Cisco runs development
  Spring Boot services.
- **Spring profile** — Named configuration bundle. `local`, `dev`, `prod`
  activate different bean sets. `LocalProfileConfig` is the class that
  wires up beans when the `local` profile is active.
- **gRPC (`.proto` files)** — Protocol Buffers / gRPC contract files.
  Typed inter-service contracts. Inventory and collector communicate this
  way almost certainly.
