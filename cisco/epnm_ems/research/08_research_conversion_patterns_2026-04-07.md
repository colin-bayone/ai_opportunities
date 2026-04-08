# 08 - Research: EPNM-to-EMS Conversion Patterns

**Source:** Web research
**Source Date:** 2026-04-07
**Document Set:** 08 (Technical Research)
**Pass:** Conversion patterns reference (Dojo -> Angular, classic view toggle)

---

## Context

This document provides a working reference for converting EPNM UI screens (Dojo/Dijit, Java/Oracle backend) to Angular components that render within the EMS shell app (Angular 21, Spring Boot/Go backend, PostgreSQL). The conversion is a UX overlay -- the backend stays as-is. Angular renders screens that replicate the EPNM "blue and white" look and feel, connected to the existing EMS REST APIs.

Key architectural facts from Set 07 meeting (2026-04-06):
- EMS frontend: Angular 21, Harbor/Magnetic design system
- EMS backend: Spring Boot + Go services, PostgreSQL
- EMS repos: Infra UI (shell), Common UI (shared components), EMS UI (feature pages)
- EPNM frontend: Dojo (legacy), blue/white theme
- ~80% of EPNM backend functionality already reimplemented in EMS
- Classic view is the default after login; toggle switches to modern Magnetic view
- Classic UI code lives within EMS UI repo (or separate repo -- decision pending)

---

## 1. Dojo to Angular Component Mapping

### 1.1 DataGrid -> Angular Material Table (mat-table)

The Dojo `dojox/grid/DataGrid` is the primary table widget in EPNM. It maps to Angular Material's `mat-table` with `MatSort` and `MatPaginator`.

**Dojo DataGrid (EPNM pattern):**

```javascript
require([
  "dojox/grid/DataGrid",
  "dojo/data/ItemFileWriteStore",
  "dojo/domReady!"
], function(DataGrid, ItemFileWriteStore) {

  var store = new ItemFileWriteStore({
    data: {
      identifier: "id",
      items: [
        { id: 1, hostname: "router-01", ipAddress: "10.0.0.1", status: "Managed", deviceType: "Cisco ASR 9000" },
        { id: 2, hostname: "switch-01", ipAddress: "10.0.0.2", status: "Managed", deviceType: "Cisco Nexus 9000" }
      ]
    }
  });

  var layout = [
    { field: "hostname", name: "Device Name", width: "200px" },
    { field: "ipAddress", name: "IP Address", width: "150px" },
    { field: "status", name: "Status", width: "100px" },
    { field: "deviceType", name: "Device Type", width: "auto",
      formatter: function(value) {
        return "<span class='device-type'>" + value + "</span>";
      }
    }
  ];

  var grid = new DataGrid({
    store: store,
    structure: layout,
    rowSelector: "20px",
    clientSort: true,
    query: { hostname: "*" }
  }, "gridDiv");
  grid.startup();
});
```

**Angular Material Table (EMS classic view equivalent):**

```typescript
// network-devices-classic.component.ts
import { Component, OnInit, ViewChild, inject } from '@angular/core';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatSort, MatSortModule } from '@angular/material/sort';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { NetworkDevice } from '../models/network-device.model';
import { InventoryService } from '../services/inventory.service';

@Component({
  selector: 'app-network-devices-classic',
  standalone: true,
  imports: [MatTableModule, MatSortModule, MatPaginatorModule],
  templateUrl: './network-devices-classic.component.html',
  styleUrls: ['./network-devices-classic.component.scss']
})
export class NetworkDevicesClassicComponent implements OnInit {
  private inventoryService = inject(InventoryService);

  displayedColumns: string[] = ['hostname', 'ipAddress', 'status', 'deviceType'];
  dataSource = new MatTableDataSource<NetworkDevice>();

  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  ngOnInit(): void {
    this.inventoryService.getNetworkDevices().subscribe(devices => {
      this.dataSource.data = devices;
    });
  }

  ngAfterViewInit(): void {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }
}
```

```html
<!-- network-devices-classic.component.html -->
<div class="epnm-table-container">
  <table mat-table [dataSource]="dataSource" matSort class="epnm-data-grid">

    <ng-container matColumnDef="hostname">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>Device Name</th>
      <td mat-cell *matCellDef="let device">
        <a class="epnm-device-link" (click)="openDeviceDetails(device)">
          {{ device.hostname }}
        </a>
      </td>
    </ng-container>

    <ng-container matColumnDef="ipAddress">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>IP Address</th>
      <td mat-cell *matCellDef="let device">{{ device.ipAddress }}</td>
    </ng-container>

    <ng-container matColumnDef="status">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>Status</th>
      <td mat-cell *matCellDef="let device">
        <span [class]="'epnm-status epnm-status--' + device.status.toLowerCase()">
          {{ device.status }}
        </span>
      </td>
    </ng-container>

    <ng-container matColumnDef="deviceType">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>Device Type</th>
      <td mat-cell *matCellDef="let device">
        <span class="epnm-device-type">{{ device.deviceType }}</span>
      </td>
    </ng-container>

    <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
    <tr mat-row *matRowDef="let row; columns: displayedColumns;"
        (click)="selectDevice(row)"
        [class.selected]="selectedDevice === row">
    </tr>
  </table>

  <mat-paginator [pageSizeOptions]="[25, 50, 100]" showFirstLastButtons>
  </mat-paginator>
</div>
```

**Key mapping notes:**
- Dojo `structure` array -> Angular column definitions via `matColumnDef`
- Dojo `formatter` function -> Angular template expressions or pipes within `*matCellDef`
- Dojo `store` -> Angular `MatTableDataSource` wrapping service data
- Dojo `clientSort: true` -> `matSort` directive + `MatSort` ViewChild
- Dojo `rowSelector` -> `(click)` event binding on `mat-row`
- Dojo `query` -> Angular service-level filtering or `dataSource.filter`

### 1.2 Dialog -> Angular Material Dialog (MatDialog)

EPNM uses `dijit/Dialog` extensively for Device 360 views and confirmation popups. These map to Angular Material's `MatDialog`.

**Dojo Dialog (EPNM pattern):**

```javascript
require([
  "dijit/Dialog",
  "dijit/form/Button",
  "dojo/dom",
  "dojo/domReady!"
], function(Dialog, Button, dom) {

  var device360Dialog = new Dialog({
    title: "Device 360 - router-01",
    content: "<div id='device360Content'></div>",
    style: "width: 800px; height: 600px;",
    onHide: function() {
      // cleanup when dialog closes
    }
  });

  // Programmatically set content
  device360Dialog.set("content", buildDevice360Content(deviceData));
  device360Dialog.show();
});
```

**Angular Material Dialog (EMS classic view equivalent):**

```typescript
// device-360-classic.component.ts (dialog component)
import { Component, inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef, MatDialogModule } from '@angular/material/dialog';
import { NetworkDevice } from '../models/network-device.model';

@Component({
  selector: 'app-device-360-classic',
  standalone: true,
  imports: [MatDialogModule],
  templateUrl: './device-360-classic.component.html',
  styleUrls: ['./device-360-classic.component.scss']
})
export class Device360ClassicComponent {
  private dialogRef = inject(MatDialogRef<Device360ClassicComponent>);
  data: { device: NetworkDevice } = inject(MAT_DIALOG_DATA);

  activeTab = 'alarms';

  close(): void {
    this.dialogRef.close();
  }

  openInterface360(interfaceData: any): void {
    // Nested dialog -- mirrors EPNM's "360 inside 360" pattern
    // Inject MatDialog to open another dialog from within this one
  }
}
```

```typescript
// Opening the dialog from the parent component
import { MatDialog } from '@angular/material/dialog';

export class NetworkDevicesClassicComponent {
  private dialog = inject(MatDialog);

  openDevice360(device: NetworkDevice): void {
    this.dialog.open(Device360ClassicComponent, {
      data: { device },
      width: '800px',
      height: '600px',
      panelClass: 'epnm-dialog-container'  // applies EPNM blue/white styling
    });
  }
}
```

**Key mapping notes:**
- Dojo `new Dialog({ content: ... })` -> `MatDialog.open(ComponentClass, config)`
- Dojo `dialog.show()` -> `dialog.open()` returns `MatDialogRef`
- Dojo `dialog.set("content", html)` -> Angular template rendering within the dialog component
- Dojo `onHide` callback -> `MatDialogRef.afterClosed().subscribe()`
- Dojo nested dialogs -> Angular can open a `MatDialog` from within another dialog component
- `panelClass` on the dialog config applies EPNM-specific CSS without affecting the global theme

### 1.3 Tree -> Angular CDK Tree / Material Tree

EPNM uses `dijit/Tree` with `ObjectStoreModel` for hierarchical views like chassis component trees and navigation menus. These map to Angular's CDK Tree (`CdkTree`) or Material Tree (`MatTree`).

**Dojo Tree (EPNM pattern):**

```javascript
require([
  "dojo/store/Memory",
  "dijit/tree/ObjectStoreModel",
  "dijit/Tree",
  "dojo/domReady!"
], function(Memory, ObjectStoreModel, Tree) {

  var store = new Memory({
    data: [
      { id: "root", name: "ASR-9000", type: "chassis" },
      { id: "slot0", name: "Slot 0 - RSP", parent: "root", type: "module" },
      { id: "slot1", name: "Slot 1 - Line Card", parent: "root", type: "module" },
      { id: "port0", name: "GigE 0/0/0", parent: "slot1", type: "port" },
      { id: "port1", name: "GigE 0/0/1", parent: "slot1", type: "port" }
    ],
    getChildren: function(object) {
      return this.query({ parent: object.id });
    }
  });

  var model = new ObjectStoreModel({
    store: store,
    query: { id: "root" },
    mayHaveChildren: function(item) {
      return item.type !== "port";
    }
  });

  var tree = new Tree({
    model: model,
    showRoot: true,
    onClick: function(item) {
      displayModuleDetails(item);
    }
  }, "chassisTree");
  tree.startup();
});
```

**Angular Material Tree (EMS classic view equivalent):**

```typescript
// chassis-tree-classic.component.ts
import { Component, OnInit, inject } from '@angular/core';
import { FlatTreeControl } from '@angular/cdk/tree';
import { MatTreeFlatDataSource, MatTreeFlattener, MatTreeModule } from '@angular/material/tree';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

interface ChassisNode {
  id: string;
  name: string;
  type: 'chassis' | 'module' | 'port';
  children?: ChassisNode[];
}

interface FlatChassisNode {
  expandable: boolean;
  name: string;
  type: string;
  level: number;
}

@Component({
  selector: 'app-chassis-tree-classic',
  standalone: true,
  imports: [MatTreeModule, MatIconModule, MatButtonModule],
  template: `
    <mat-tree [dataSource]="dataSource" [treeControl]="treeControl" class="epnm-tree">
      <mat-tree-node *matTreeNodeDef="let node" matTreeNodePadding>
        <button mat-icon-button disabled></button>
        <span class="epnm-tree-node epnm-tree-node--{{node.type}}"
              (click)="selectNode(node)">
          {{ node.name }}
        </span>
      </mat-tree-node>

      <mat-tree-node *matTreeNodeDef="let node; when: hasChild" matTreeNodePadding>
        <button mat-icon-button matTreeNodeToggle>
          <mat-icon>
            {{ treeControl.isExpanded(node) ? 'expand_more' : 'chevron_right' }}
          </mat-icon>
        </button>
        <span class="epnm-tree-node epnm-tree-node--{{node.type}}"
              (click)="selectNode(node)">
          {{ node.name }}
        </span>
      </mat-tree-node>
    </mat-tree>
  `
})
export class ChassisTreeClassicComponent implements OnInit {
  private transformer = (node: ChassisNode, level: number): FlatChassisNode => ({
    expandable: !!node.children && node.children.length > 0,
    name: node.name,
    type: node.type,
    level: level,
  });

  treeControl = new FlatTreeControl<FlatChassisNode>(
    node => node.level,
    node => node.expandable
  );

  treeFlattener = new MatTreeFlattener(
    this.transformer,
    node => node.level,
    node => node.expandable,
    node => node.children
  );

  dataSource = new MatTreeFlatDataSource(this.treeControl, this.treeFlattener);

  hasChild = (_: number, node: FlatChassisNode) => node.expandable;

  ngOnInit(): void {
    // Load chassis data from EMS API and assign to dataSource.data
  }

  selectNode(node: FlatChassisNode): void {
    // Display module/port details in the detail panel
  }
}
```

**Key mapping notes:**
- Dojo `Memory` store with `getChildren` -> Angular nested data structure with `children` array
- Dojo `ObjectStoreModel` -> Angular `MatTreeFlattener` + `MatTreeFlatDataSource`
- Dojo `mayHaveChildren` -> Angular `hasChild` function
- Dojo `onClick` -> Angular `(click)` event binding on tree node elements
- Dojo `tree.startup()` -> Angular handles rendering through data binding
- Dojo `showRoot: true` -> Angular controls root visibility through data structure

### 1.4 Form Widgets -> Angular Reactive Forms

EPNM uses Dijit form widgets (`TextBox`, `FilteringSelect`, `NumberSpinner`, `CheckBox`) extensively in the Add Device wizard, filtering panels, and configuration forms. These map to Angular Reactive Forms with `FormControl`, `FormGroup`, and `FormBuilder`.

**Dojo Form Widgets (EPNM pattern):**

```javascript
require([
  "dijit/form/TextBox",
  "dijit/form/FilteringSelect",
  "dijit/form/CheckBox",
  "dojo/store/Memory",
  "dojo/domReady!"
], function(TextBox, FilteringSelect, CheckBox, Memory) {

  var ipInput = new TextBox({
    name: "ipAddress",
    value: "",
    placeHolder: "Enter IP Address",
    required: true,
    intermediateChanges: true,
    onChange: function(value) {
      validateIPAddress(value);
    }
  }, "ipAddressField");

  var deviceTypeStore = new Memory({
    data: [
      { id: "asr9k", name: "Cisco ASR 9000" },
      { id: "nexus9k", name: "Cisco Nexus 9000" },
      { id: "ncs5500", name: "Cisco NCS 5500" }
    ]
  });

  var deviceTypeSelect = new FilteringSelect({
    name: "deviceType",
    store: deviceTypeStore,
    searchAttr: "name",
    placeHolder: "Select Device Type",
    required: true
  }, "deviceTypeField");

  var snmpEnabled = new CheckBox({
    name: "snmpEnabled",
    checked: true,
    onChange: function(checked) {
      toggleSNMPFields(checked);
    }
  }, "snmpCheckbox");
});
```

**Angular Reactive Forms (EMS classic view equivalent):**

```typescript
// add-device-classic.component.ts
import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatStepperModule } from '@angular/material/stepper';

@Component({
  selector: 'app-add-device-classic',
  standalone: true,
  imports: [
    ReactiveFormsModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatCheckboxModule, MatStepperModule
  ],
  templateUrl: './add-device-classic.component.html',
  styleUrls: ['./add-device-classic.component.scss']
})
export class AddDeviceClassicComponent implements OnInit {
  private fb = inject(FormBuilder);

  // Step 1: Device identification
  deviceInfoForm!: FormGroup;
  // Step 2: Credentials
  credentialsForm!: FormGroup;

  deviceTypes = [
    { id: 'asr9k', name: 'Cisco ASR 9000' },
    { id: 'nexus9k', name: 'Cisco Nexus 9000' },
    { id: 'ncs5500', name: 'Cisco NCS 5500' }
  ];

  ngOnInit(): void {
    this.deviceInfoForm = this.fb.group({
      ipAddress: ['', [Validators.required, this.ipAddressValidator]],
      deviceType: ['', Validators.required]
    });

    this.credentialsForm = this.fb.group({
      snmpEnabled: [true],
      snmpCommunity: [''],
      telnetEnabled: [false],
      telnetUsername: [''],
      telnetPassword: [''],
      httpEnabled: [false]
    });

    // React to snmpEnabled changes (replaces Dojo onChange callback)
    this.credentialsForm.get('snmpEnabled')!.valueChanges.subscribe(enabled => {
      const snmpCommunity = this.credentialsForm.get('snmpCommunity')!;
      if (enabled) {
        snmpCommunity.setValidators(Validators.required);
      } else {
        snmpCommunity.clearValidators();
      }
      snmpCommunity.updateValueAndValidity();
    });
  }

  private ipAddressValidator(control: any) {
    const ipRegex = /^(\d{1,3}\.){3}\d{1,3}$/;
    return ipRegex.test(control.value) ? null : { invalidIP: true };
  }
}
```

```html
<!-- add-device-classic.component.html -->
<mat-stepper linear class="epnm-stepper">
  <mat-step [stepControl]="deviceInfoForm" label="Device Information">
    <form [formGroup]="deviceInfoForm" class="epnm-form">
      <mat-form-field class="epnm-form-field">
        <mat-label>IP Address</mat-label>
        <input matInput formControlName="ipAddress" placeholder="Enter IP Address">
        <mat-error *ngIf="deviceInfoForm.get('ipAddress')?.hasError('invalidIP')">
          Invalid IP address format
        </mat-error>
      </mat-form-field>

      <mat-form-field class="epnm-form-field">
        <mat-label>Device Type</mat-label>
        <mat-select formControlName="deviceType">
          @for (type of deviceTypes; track type.id) {
            <mat-option [value]="type.id">{{ type.name }}</mat-option>
          }
        </mat-select>
      </mat-form-field>
    </form>
  </mat-step>

  <mat-step [stepControl]="credentialsForm" label="Credentials">
    <form [formGroup]="credentialsForm" class="epnm-form">
      <mat-checkbox formControlName="snmpEnabled" class="epnm-checkbox">
        SNMP
      </mat-checkbox>
      @if (credentialsForm.get('snmpEnabled')?.value) {
        <mat-form-field class="epnm-form-field">
          <mat-label>SNMP Community</mat-label>
          <input matInput formControlName="snmpCommunity">
        </mat-form-field>
      }
    </form>
  </mat-step>
</mat-stepper>
```

**Key mapping notes:**
- Dojo `TextBox` -> `<input matInput>` with `formControlName`
- Dojo `FilteringSelect` with `store` -> `<mat-select>` with `<mat-option>` loop (or `mat-autocomplete` for type-ahead filtering)
- Dojo `CheckBox` with `onChange` -> `formControlName` + `valueChanges` subscription
- Dojo `required: true` -> `Validators.required` in FormGroup definition
- Dojo `intermediateChanges` -> `valueChanges` Observable on the FormControl (emits on every keystroke by default)
- Dojo step-by-step wizard -> `<mat-stepper>` with `linear` mode
- Dojo `placeHolder` -> `placeholder` attribute on `<input>` or `<mat-label>` directive

### 1.5 Complete Dojo-to-Angular Widget Mapping Table

| Dojo Widget | Angular Equivalent | Notes |
|---|---|---|
| `dojox/grid/DataGrid` | `mat-table` + `MatSort` + `MatPaginator` | See 1.1 above |
| `dgrid/Grid` | `mat-table` | Same mapping, dgrid is the newer Dojo grid |
| `dijit/Dialog` | `MatDialog.open()` | See 1.2 above |
| `dijit/TooltipDialog` | `MatMenu` or `cdkOverlayOrigin` | For popup panels like Device 360 |
| `dijit/Tree` | `MatTree` / `CdkTree` | See 1.3 above |
| `dijit/form/TextBox` | `<input matInput>` + `FormControl` | See 1.4 above |
| `dijit/form/ValidationTextBox` | `FormControl` + `Validators` | Validators replace regex property |
| `dijit/form/FilteringSelect` | `<mat-select>` or `<mat-autocomplete>` | Autocomplete for type-ahead behavior |
| `dijit/form/ComboBox` | `<mat-autocomplete>` + free text | Allows non-listed values |
| `dijit/form/Select` | `<mat-select>` | Simple dropdown |
| `dijit/form/CheckBox` | `<mat-checkbox>` | Use with `formControlName` |
| `dijit/form/RadioButton` | `<mat-radio-group>` + `<mat-radio-button>` | Wrap in FormControl |
| `dijit/form/NumberSpinner` | `<input matInput type="number">` | Add step buttons manually if needed |
| `dijit/form/DateTextBox` | `<mat-datepicker>` | Use `MatDatepickerModule` |
| `dijit/form/Button` | `<button mat-button>` or `<button mat-raised-button>` | Style variants via mat- prefix |
| `dijit/ProgressBar` | `<mat-progress-bar>` | Mode: determinate, indeterminate, buffer |
| `dijit/TabContainer` | `<mat-tab-group>` + `<mat-tab>` | Used in Device 360 tabs |
| `dijit/layout/ContentPane` | Angular component with `<ng-content>` | Content projection replaces ContentPane |
| `dijit/layout/BorderContainer` | CSS Grid or Flexbox layout | No direct widget; use CSS layout |
| `dijit/layout/AccordionContainer` | `<mat-accordion>` + `<mat-expansion-panel>` | Collapsible sections |
| `dijit/Toolbar` | `<mat-toolbar>` | Action bar above tables |
| `dijit/Menu` / `dijit/MenuItem` | `<mat-menu>` + `<mat-menu-item>` | Context menus, action menus |
| `dijit/Tooltip` | `matTooltip` directive | Inline tooltip |
| `dojox/widget/Toaster` | `MatSnackBar` | Toast notifications |

---

## 2. AMD to ES6 Module Migration

### 2.1 Pattern Mapping

Dojo uses AMD (Asynchronous Module Definition) via `require()` and `define()`. Angular uses ES6 modules via `import`/`export` with TypeScript, plus Angular's dependency injection (DI) system for services.

**Dojo AMD pattern (EPNM):**

```javascript
// NetworkDevicesView.js
define([
  "dojo/_base/declare",
  "dijit/_WidgetBase",
  "dijit/_TemplatedMixin",
  "dojo/store/JsonRest",
  "dojo/topic",
  "dojo/on",
  "dojo/dom-class",
  "dojo/text!./templates/NetworkDevicesView.html"
], function(
  declare,
  _WidgetBase,
  _TemplatedMixin,
  JsonRest,
  topic,
  on,
  domClass,
  template
) {
  return declare("epnm.views.NetworkDevicesView", [_WidgetBase, _TemplatedMixin], {
    templateString: template,

    postCreate: function() {
      this.inherited(arguments);
      this._store = new JsonRest({ target: "/api/v1/devices" });
      this._loadDevices();
    },

    _loadDevices: function() {
      this._store.query({}).then(function(devices) {
        this._renderGrid(devices);
      }.bind(this));
    },

    destroy: function() {
      // cleanup
      this.inherited(arguments);
    }
  });
});
```

**Angular ES6 module equivalent:**

```typescript
// network-devices-classic.component.ts
import { Component, OnInit, OnDestroy, inject } from '@angular/core';
import { Subject, takeUntil } from 'rxjs';
import { InventoryService } from '../services/inventory.service';
import { NetworkDevice } from '../models/network-device.model';

@Component({
  selector: 'app-network-devices-classic',
  standalone: true,
  imports: [/* material modules */],
  templateUrl: './network-devices-classic.component.html',
  styleUrls: ['./network-devices-classic.component.scss']
})
export class NetworkDevicesClassicComponent implements OnInit, OnDestroy {
  private inventoryService = inject(InventoryService);
  private destroy$ = new Subject<void>();

  devices: NetworkDevice[] = [];

  ngOnInit(): void {
    this.loadDevices();
  }

  private loadDevices(): void {
    this.inventoryService.getNetworkDevices()
      .pipe(takeUntil(this.destroy$))
      .subscribe(devices => {
        this.devices = devices;
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### 2.2 Key Conversion Rules

| AMD Pattern | ES6/Angular Equivalent |
|---|---|
| `define(["dep1", "dep2"], function(dep1, dep2) { ... })` | `import { dep1 } from 'dep1'; import { dep2 } from 'dep2';` |
| `require(["module"], function(Module) { ... })` | `import { Module } from './module';` (static) or `import('./module')` (dynamic/lazy) |
| `dojo/_base/declare("ClassName", [Base1, Base2], { ... })` | `class ClassName extends Base1 implements Interface2 { ... }` |
| `dojo/text!./template.html` (plugin-based text loading) | `templateUrl: './template.html'` in `@Component` decorator |
| `dojo/i18n!./nls/strings` | Angular `@ngx-translate` or built-in `$localize` |
| `return declare(...)` (module exports single class) | `export class ...` or `export default class ...` |
| `this.inherited(arguments)` (super call) | `super.methodName()` |
| Dependencies injected via `define()` callback args | Services injected via `inject()` function or constructor DI |

### 2.3 Automated Conversion Tools

The npm package `amd-to-es6` can perform bulk conversion of AMD `define()` calls to ES6 `import`/`export` syntax. This is useful for initial mechanical transformation of EPNM utility modules, though all resulting code will still need TypeScript conversion and Angular adaptation.

```bash
# Install the conversion tool
npm install -g amd-to-es6

# Convert a single file
amd-to-es6 src/legacy/NetworkDevicesView.js
```

The tool handles the `define([deps], function(args) { })` -> `import/export` transformation but does not handle Dojo-specific patterns like `declare()`, `this.inherited()`, or Dijit widget lifecycle methods.

---

## 3. Data Binding Patterns

### 3.1 Dojo Property Watch vs. Angular Binding

Dojo widgets use `get()`, `set()`, and `watch()` for property management. These are defined on `dojo/Stateful`, which `dijit/_WidgetBase` extends. Angular uses template binding, `@Input()`/`@Output()` (or signal-based `input()`/`output()`), and Reactive Forms.

**Dojo watch pattern (EPNM):**

```javascript
// Setting and watching widget properties
var widget = new MyWidget({
  deviceName: "router-01",
  isOnline: true
});

// Programmatic get/set
var name = widget.get("deviceName");
widget.set("isOnline", false);

// Watch for changes
widget.watch("isOnline", function(property, oldValue, newValue) {
  console.log(property + " changed from " + oldValue + " to " + newValue);
  updateStatusIndicator(newValue);
});

// Custom setter (inside widget definition)
declare("DeviceWidget", [_WidgetBase], {
  _setDeviceNameAttr: function(value) {
    this._set("deviceName", value);  // triggers watch callbacks
    this.domNode.querySelector(".device-name").textContent = value;
  }
});
```

**Angular equivalent patterns:**

```typescript
// Pattern 1: Template binding (most common)
@Component({
  template: `
    <span class="device-name">{{ deviceName }}</span>
    <span [class.online]="isOnline">{{ isOnline ? 'Online' : 'Offline' }}</span>
  `
})
export class DeviceWidgetComponent {
  deviceName = 'router-01';
  isOnline = true;

  // Angular change detection handles DOM updates automatically
  updateStatus(online: boolean): void {
    this.isOnline = online;  // template re-renders automatically
  }
}

// Pattern 2: Signal-based inputs (Angular 17+, preferred for Angular 21)
@Component({
  template: `
    <span class="device-name">{{ deviceName() }}</span>
    <span [class.online]="isOnline()">{{ isOnline() ? 'Online' : 'Offline' }}</span>
  `
})
export class DeviceWidgetComponent {
  deviceName = input.required<string>();      // replaces @Input()
  isOnline = input<boolean>(true);            // with default value
  statusChange = output<boolean>();           // replaces @Output()

  // effect() replaces watch() -- runs when signal values change
  constructor() {
    effect(() => {
      console.log('isOnline changed to:', this.isOnline());
    });
  }
}

// Pattern 3: model() for two-way binding (Angular 17.2+)
@Component({
  template: `
    <input [ngModel]="filterText()" (ngModelChange)="filterText.set($event)">
  `
})
export class DeviceFilterComponent {
  filterText = model<string>('');  // parent can bind with [(filterText)]
}
```

### 3.2 Conversion Summary

| Dojo Pattern | Angular Equivalent | When to Use |
|---|---|---|
| `widget.get("prop")` | `this.prop` or `this.prop()` (signal) | Reading component state |
| `widget.set("prop", value)` | `this.prop = value` or `this.prop.set(value)` | Setting component state |
| `widget.watch("prop", callback)` | `effect(() => { ... })` (signal) or `ngOnChanges()` | Reacting to property changes |
| `_setFooAttr(value)` custom setter | `set` accessor, or `effect()` with side effects | Custom logic on property change |
| Template substitution `${prop}` | `{{ prop }}` interpolation or `[attr]="prop"` | Rendering values in templates |
| `data-dojo-attach-point` | `@ViewChild()` / `#templateRef` | Getting DOM element references |
| `data-dojo-attach-event` | `(event)="handler()"` | Binding DOM events |

---

## 4. Event Handling

### 4.1 Dojo Events vs. Angular Events

Dojo has three event mechanisms: `dojo/on` for DOM events, `dojo/aspect` for method interception, and `dojo/topic` for pub/sub messaging. Angular maps these to template event binding, decorators, and RxJS Subjects.

**Dojo DOM events (dojo/on):**

```javascript
require(["dojo/on", "dojo/dom"], function(on, dom) {
  // DOM event listener
  var handle = on(dom.byId("refreshBtn"), "click", function(evt) {
    refreshDeviceList();
  });

  // Later: remove the listener
  handle.remove();
});
```

**Angular template event binding equivalent:**

```html
<!-- Direct template binding -- preferred approach -->
<button (click)="refreshDeviceList()" class="epnm-btn">Refresh</button>
```

**Dojo method interception (dojo/aspect):**

```javascript
require(["dojo/aspect"], function(aspect) {
  // Run code after a method executes
  aspect.after(deviceGrid, "onRowClick", function(row) {
    updateDetailPanel(row.data);
  });

  // Run code before a method executes
  aspect.before(deviceStore, "put", function(object) {
    object.lastModified = new Date();
    return [object];
  });
});
```

**Angular equivalent (using RxJS or interceptors):**

```typescript
// For method interception patterns, use Angular's HTTP interceptors
// or RxJS pipe operators
@Injectable()
export class TimestampInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (req.method === 'PUT' || req.method === 'POST') {
      const modified = req.clone({
        body: { ...req.body, lastModified: new Date().toISOString() }
      });
      return next.handle(modified);
    }
    return next.handle(req);
  }
}
```

### 4.2 Pub/Sub: dojo/topic vs. RxJS Subject Services

Dojo's `dojo/topic` provides a global event bus for cross-component communication. In Angular, this pattern maps to shared services with RxJS `Subject` or `BehaviorSubject`.

**Dojo pub/sub (EPNM pattern):**

```javascript
// Publisher (e.g., device list component)
require(["dojo/topic"], function(topic) {
  topic.publish("device/selected", { deviceId: "router-01", ip: "10.0.0.1" });
});

// Subscriber (e.g., detail panel component)
require(["dojo/topic"], function(topic) {
  var handle = topic.subscribe("device/selected", function(deviceData) {
    updateDetailPanel(deviceData);
  });

  // Cleanup
  handle.remove();
});
```

**Angular shared service with Subject:**

```typescript
// event-bus.service.ts (replaces dojo/topic)
import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';

export interface DeviceSelectedEvent {
  deviceId: string;
  ip: string;
}

@Injectable({ providedIn: 'root' })
export class EventBusService {
  // Each "topic" becomes a typed Subject
  private deviceSelected$ = new Subject<DeviceSelectedEvent>();
  private alarmAcknowledged$ = new Subject<string>();

  // Publish
  emitDeviceSelected(event: DeviceSelectedEvent): void {
    this.deviceSelected$.next(event);
  }

  // Subscribe (returns Observable for the consumer to subscribe to)
  onDeviceSelected(): Observable<DeviceSelectedEvent> {
    return this.deviceSelected$.asObservable();
  }

  emitAlarmAcknowledged(alarmId: string): void {
    this.alarmAcknowledged$.next(alarmId);
  }

  onAlarmAcknowledged(): Observable<string> {
    return this.alarmAcknowledged$.asObservable();
  }
}
```

```typescript
// Publisher component
export class NetworkDevicesClassicComponent {
  private eventBus = inject(EventBusService);

  selectDevice(device: NetworkDevice): void {
    this.eventBus.emitDeviceSelected({
      deviceId: device.id,
      ip: device.ipAddress
    });
  }
}

// Subscriber component
export class DeviceDetailPanelComponent implements OnInit, OnDestroy {
  private eventBus = inject(EventBusService);
  private destroy$ = new Subject<void>();

  ngOnInit(): void {
    this.eventBus.onDeviceSelected()
      .pipe(takeUntil(this.destroy$))
      .subscribe(event => {
        this.loadDeviceDetails(event.deviceId);
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### 4.3 Component-to-Component Communication Patterns

| Dojo Pattern | Angular Equivalent | Scope |
|---|---|---|
| `dojo/topic.publish` / `topic.subscribe` | Shared service with `Subject` | Cross-component (any to any) |
| `dojo/on(domNode, event, handler)` | `(event)="handler()"` template binding | Single component DOM events |
| `widget.emit("customEvent", data)` | `@Output() customEvent = new EventEmitter()` | Child to parent |
| `dojo/aspect.after(obj, method, callback)` | RxJS `tap()` operator in pipe, or HTTP interceptor | Method interception |
| `dojo/Evented` base class | Service extending `Subject` | Event-emitting objects |
| Parent calling child method directly | `@ViewChild(ChildComponent)` | Parent to child (imperative) |
| Shared data store | Shared service with `BehaviorSubject` | State shared across components |

---

## 5. Lifecycle Method Mapping

### 5.1 Dojo Widget Lifecycle

Dojo widgets (based on `dijit/_WidgetBase`) follow this lifecycle:

1. **`constructor(params, srcNodeRef)`** -- Object instantiation. Mixes in params.
2. **`postMixInProperties()`** -- Called after properties from params are mixed in but before the DOM template is created. Used to compute derived properties.
3. **`buildRendering()`** -- Creates the DOM tree from the template string. Sets `this.domNode`.
4. **`postCreate()`** -- Called after the DOM tree is created but before it is placed in the document. Most initialization code goes here. This is the most commonly used lifecycle method.
5. **`startup()`** -- Called after the widget and its children are placed in the document. Use for layout calculations that require rendered DOM dimensions.
6. **`destroy()`** -- Cleanup. Remove event listeners, destroy child widgets, release resources.

### 5.2 Angular Component Lifecycle

Angular components follow this lifecycle (key hooks only):

1. **`constructor()`** -- Dependency injection happens here. Avoid heavy logic.
2. **`ngOnChanges(changes)`** -- Called when `@Input()` values change. Provides `SimpleChanges` object with previous and current values.
3. **`ngOnInit()`** -- Called once after the first `ngOnChanges`. Primary initialization: load data, set up subscriptions.
4. **`ngAfterContentInit()`** -- Called after content projection (`<ng-content>`) is initialized.
5. **`ngAfterViewInit()`** -- Called after the component's view and child views are initialized. Use for DOM-dependent setup (accessing `@ViewChild` elements).
6. **`ngOnDestroy()`** -- Cleanup. Unsubscribe from Observables, remove event listeners.

### 5.3 Mapping Table

| Dojo Lifecycle | Angular Lifecycle | When / Purpose |
|---|---|---|
| `constructor(params)` | `constructor()` | Object creation, DI. In Angular, avoid side effects here. |
| `postMixInProperties()` | `ngOnChanges()` (first call) or field initializers | Compute derived properties from inputs before rendering. |
| `buildRendering()` | (handled by Angular's template compiler) | DOM creation. No Angular equivalent -- Angular's renderer handles this. |
| `postCreate()` | **`ngOnInit()`** | **Primary initialization.** This is the main mapping. Most Dojo `postCreate` code moves to `ngOnInit`. |
| `startup()` | **`ngAfterViewInit()`** | DOM-dependent initialization. Use when you need to measure DOM elements, initialize third-party libraries on rendered elements, or access `@ViewChild` references. |
| `destroy()` | **`ngOnDestroy()`** | Cleanup. Unsubscribe, release resources. In Angular, use `takeUntil(this.destroy$)` pattern or `DestroyRef`. |
| `resize()` (dijit layout) | `@HostListener('window:resize')` or `ResizeObserver` | Window/container resize handling. |

### 5.4 Concrete Conversion Example

**Dojo widget with full lifecycle (EPNM):**

```javascript
define([
  "dojo/_base/declare",
  "dijit/_WidgetBase",
  "dijit/_TemplatedMixin",
  "dojo/on",
  "dojo/topic",
  "dojo/store/JsonRest",
  "dojo/text!./templates/AlarmPanel.html"
], function(declare, _WidgetBase, _TemplatedMixin, on, topic, JsonRest, template) {

  return declare("epnm.alarms.AlarmPanel", [_WidgetBase, _TemplatedMixin], {

    templateString: template,
    deviceId: null,
    refreshInterval: 30000,

    postMixInProperties: function() {
      this.inherited(arguments);
      this._alarmStore = new JsonRest({ target: "/api/v1/alarms" });
    },

    postCreate: function() {
      this.inherited(arguments);
      this._loadAlarms();
      this._topicHandle = topic.subscribe("device/selected", function(data) {
        this.set("deviceId", data.deviceId);
        this._loadAlarms();
      }.bind(this));
    },

    startup: function() {
      this.inherited(arguments);
      this._resizeGrid();
      this._timer = setInterval(this._loadAlarms.bind(this), this.refreshInterval);
    },

    _loadAlarms: function() {
      if (!this.deviceId) return;
      this._alarmStore.query({ deviceId: this.deviceId }).then(function(alarms) {
        this._renderAlarms(alarms);
      }.bind(this));
    },

    destroy: function() {
      if (this._topicHandle) this._topicHandle.remove();
      if (this._timer) clearInterval(this._timer);
      this.inherited(arguments);
    }
  });
});
```

**Angular equivalent:**

```typescript
import { Component, OnInit, AfterViewInit, OnDestroy, input, inject } from '@angular/core';
import { Subject, interval, switchMap, takeUntil, filter } from 'rxjs';
import { AlarmService } from '../services/alarm.service';
import { EventBusService } from '../services/event-bus.service';
import { Alarm } from '../models/alarm.model';

@Component({
  selector: 'app-alarm-panel-classic',
  standalone: true,
  imports: [/* material modules */],
  templateUrl: './alarm-panel-classic.component.html',
  styleUrls: ['./alarm-panel-classic.component.scss']
})
export class AlarmPanelClassicComponent implements OnInit, AfterViewInit, OnDestroy {
  // DI -- replaces postMixInProperties store creation
  private alarmService = inject(AlarmService);
  private eventBus = inject(EventBusService);
  private destroy$ = new Subject<void>();

  // Properties -- replaces Dojo widget properties
  deviceId: string | null = null;
  refreshInterval = 30000;
  alarms: Alarm[] = [];

  // ngOnInit -- replaces postCreate
  ngOnInit(): void {
    this.loadAlarms();

    // Replaces topic.subscribe("device/selected", ...)
    this.eventBus.onDeviceSelected()
      .pipe(takeUntil(this.destroy$))
      .subscribe(event => {
        this.deviceId = event.deviceId;
        this.loadAlarms();
      });

    // Replaces setInterval in startup -- auto-refresh with RxJS
    interval(this.refreshInterval)
      .pipe(
        filter(() => this.deviceId !== null),
        switchMap(() => this.alarmService.getAlarms(this.deviceId!)),
        takeUntil(this.destroy$)
      )
      .subscribe(alarms => {
        this.alarms = alarms;
      });
  }

  // ngAfterViewInit -- replaces startup (DOM-dependent operations)
  ngAfterViewInit(): void {
    this.resizeGrid();
  }

  private loadAlarms(): void {
    if (!this.deviceId) return;
    this.alarmService.getAlarms(this.deviceId)
      .pipe(takeUntil(this.destroy$))
      .subscribe(alarms => {
        this.alarms = alarms;
      });
  }

  private resizeGrid(): void {
    // DOM-dependent layout calculations
  }

  // ngOnDestroy -- replaces destroy
  // takeUntil(destroy$) handles all subscription cleanup automatically
  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

---

## 6. State Management

### 6.1 Dojo Stores vs. Angular Services

Dojo's data layer uses `dojo/store` implementations (`Memory`, `JsonRest`, `Cache`, `Observable`). In Angular, these patterns map to injectable services using `HttpClient` for server communication and `BehaviorSubject` for local state management.

### 6.2 Store-by-Store Mapping

**dojo/store/Memory -> Angular service with local state:**

```javascript
// Dojo Memory store
require(["dojo/store/Memory"], function(Memory) {
  var deviceStore = new Memory({
    data: [
      { id: 1, name: "router-01", status: "online" },
      { id: 2, name: "switch-01", status: "offline" }
    ]
  });

  // CRUD operations
  var device = deviceStore.get(1);
  deviceStore.put({ id: 1, name: "router-01", status: "offline" });
  deviceStore.add({ id: 3, name: "router-02", status: "online" });
  deviceStore.remove(2);
  var results = deviceStore.query({ status: "online" });
});
```

```typescript
// Angular equivalent -- in-memory state service
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

export interface NetworkDevice {
  id: number;
  name: string;
  status: string;
}

@Injectable({ providedIn: 'root' })
export class DeviceStateService {
  private devices$ = new BehaviorSubject<NetworkDevice[]>([
    { id: 1, name: 'router-01', status: 'online' },
    { id: 2, name: 'switch-01', status: 'offline' }
  ]);

  // Read
  getDevices(): Observable<NetworkDevice[]> {
    return this.devices$.asObservable();
  }

  getDevice(id: number): NetworkDevice | undefined {
    return this.devices$.value.find(d => d.id === id);
  }

  // Query (replaces store.query)
  queryDevices(filter: Partial<NetworkDevice>): Observable<NetworkDevice[]> {
    return this.devices$.pipe(
      map(devices => devices.filter(d =>
        Object.entries(filter).every(([key, val]) =>
          d[key as keyof NetworkDevice] === val
        )
      ))
    );
  }

  // Update (replaces store.put)
  updateDevice(device: NetworkDevice): void {
    const current = this.devices$.value;
    const index = current.findIndex(d => d.id === device.id);
    if (index >= 0) {
      current[index] = device;
      this.devices$.next([...current]);
    }
  }

  // Add (replaces store.add)
  addDevice(device: NetworkDevice): void {
    this.devices$.next([...this.devices$.value, device]);
  }

  // Remove (replaces store.remove)
  removeDevice(id: number): void {
    this.devices$.next(this.devices$.value.filter(d => d.id !== id));
  }
}
```

**dojo/store/JsonRest -> Angular service with HttpClient:**

```javascript
// Dojo JsonRest store
require(["dojo/store/JsonRest"], function(JsonRest) {
  var deviceStore = new JsonRest({
    target: "/webacs/api/v4/data/Devices",
    idProperty: "deviceId"
  });

  // GET /webacs/api/v4/data/Devices
  deviceStore.query({ deviceType: "router" }).then(function(devices) {
    renderDevices(devices);
  });

  // GET /webacs/api/v4/data/Devices/42
  deviceStore.get(42).then(function(device) {
    showDeviceDetails(device);
  });

  // PUT /webacs/api/v4/data/Devices/42
  deviceStore.put(updatedDevice);

  // POST /webacs/api/v4/data/Devices
  deviceStore.add(newDevice);

  // DELETE /webacs/api/v4/data/Devices/42
  deviceStore.remove(42);
});
```

```typescript
// Angular equivalent -- HttpClient service
import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class InventoryService {
  private http = inject(HttpClient);

  // NOTE: This calls the EMS REST API, NOT the old EPNM API.
  // The EMS API endpoints serve the same data from PostgreSQL.
  private baseUrl = '/api/ems/v1/devices';

  // GET -- replaces store.query()
  getNetworkDevices(filters?: Record<string, string>): Observable<NetworkDevice[]> {
    let params = new HttpParams();
    if (filters) {
      Object.entries(filters).forEach(([key, value]) => {
        params = params.set(key, value);
      });
    }
    return this.http.get<NetworkDevice[]>(this.baseUrl, { params });
  }

  // GET by ID -- replaces store.get()
  getDevice(id: number): Observable<NetworkDevice> {
    return this.http.get<NetworkDevice>(`${this.baseUrl}/${id}`);
  }

  // PUT -- replaces store.put()
  updateDevice(device: NetworkDevice): Observable<NetworkDevice> {
    return this.http.put<NetworkDevice>(
      `${this.baseUrl}/${device.id}`, device
    );
  }

  // POST -- replaces store.add()
  addDevice(device: Omit<NetworkDevice, 'id'>): Observable<NetworkDevice> {
    return this.http.post<NetworkDevice>(this.baseUrl, device);
  }

  // DELETE -- replaces store.remove()
  removeDevice(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
```

**dojo/store/Cache (Memory + JsonRest combo) -> Angular service with caching:**

```typescript
// Angular equivalent of dojo/store/Cache wrapping JsonRest with Memory
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, of, tap } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CachedInventoryService {
  private http = inject(HttpClient);
  private cache$ = new BehaviorSubject<NetworkDevice[] | null>(null);
  private baseUrl = '/api/ems/v1/devices';

  getNetworkDevices(): Observable<NetworkDevice[]> {
    // Return cache if available (replaces Memory store in Cache wrapper)
    if (this.cache$.value) {
      return of(this.cache$.value);
    }
    // Otherwise fetch from server (replaces JsonRest master store)
    return this.http.get<NetworkDevice[]>(this.baseUrl).pipe(
      tap(devices => this.cache$.next(devices))
    );
  }

  // Invalidate cache on mutations (replaces Observable wrapper notifications)
  updateDevice(device: NetworkDevice): Observable<NetworkDevice> {
    return this.http.put<NetworkDevice>(
      `${this.baseUrl}/${device.id}`, device
    ).pipe(
      tap(() => this.cache$.next(null))  // invalidate cache
    );
  }
}
```

**dojo/store/Observable -> Angular BehaviorSubject with change notifications:**

```javascript
// Dojo Observable store -- wraps another store to add change notifications
require(["dojo/store/Memory", "dojo/store/Observable"], function(Memory, Observable) {
  var store = new Observable(new Memory({ data: deviceData }));

  var results = store.query({ status: "online" });
  results.observe(function(object, removedFrom, insertedInto) {
    if (removedFrom > -1) {
      // item removed from result set
    }
    if (insertedInto > -1) {
      // item added to result set
    }
  });
});
```

```typescript
// Angular equivalent -- the BehaviorSubject pattern already provides
// change notification via Observable subscription. Components that
// subscribe to the service's Observable are automatically notified
// when data changes.

// In the component:
export class DeviceListComponent implements OnInit, OnDestroy {
  private deviceState = inject(DeviceStateService);
  private destroy$ = new Subject<void>();

  devices: NetworkDevice[] = [];

  ngOnInit(): void {
    // This automatically receives notifications when data changes
    // (replaces dojo/store/Observable.observe)
    this.deviceState.getDevices()
      .pipe(takeUntil(this.destroy$))
      .subscribe(devices => {
        this.devices = devices;
        // DOM updates happen automatically via Angular change detection
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### 6.3 Store Mapping Summary

| Dojo Store | Angular Equivalent | Purpose |
|---|---|---|
| `dojo/store/Memory` | Service with `BehaviorSubject<T[]>` | Client-side in-memory data |
| `dojo/store/JsonRest` | Service with `HttpClient` | Server-side REST data access |
| `dojo/store/Cache` | Service with `BehaviorSubject` + `HttpClient` + cache logic | Caching layer over server data |
| `dojo/store/Observable` | `BehaviorSubject` (inherently observable) | Change notifications on data mutations |
| `store.query(filter)` | `HttpClient.get(url, { params })` or `BehaviorSubject.pipe(map(filter))` | Querying/filtering data |
| `store.get(id)` | `HttpClient.get(url/id)` or `BehaviorSubject.value.find()` | Single item retrieval |
| `store.put(item)` | `HttpClient.put()` + `BehaviorSubject.next()` | Update item |
| `store.add(item)` | `HttpClient.post()` + `BehaviorSubject.next()` | Create item |
| `store.remove(id)` | `HttpClient.delete()` + `BehaviorSubject.next()` | Delete item |

---

## 7. Theming and Styling: Classic View Toggle

### 7.1 The Requirement

From Set 07 meeting (Akhil's statement): "The default, once I log into the Crosswork UI, the default will be showing the EPNM theme. Basically the left menu and the other area should be the EPNM current feel should be shown instead of Magnetic."

Two visual modes must coexist within the same Angular application:
1. **Classic (EPNM):** Blue/white color scheme, legacy layout, left navigation panel, Dojo-era visual density
2. **Modern (EMS/Magnetic):** Harbor/Magnetic design system, current Crosswork UI look

### 7.2 CSS Custom Properties Architecture

The theme toggle should use CSS custom properties (variables) defined on the document root element. This allows instant switching without page reload.

**Define the two theme palettes:**

```scss
// styles/themes/_epnm-classic.scss
:root[data-theme="classic"] {
  // EPNM blue/white color palette
  --theme-primary: #003366;           // EPNM dark blue
  --theme-primary-light: #0066cc;     // EPNM medium blue
  --theme-primary-dark: #002244;      // EPNM navy
  --theme-accent: #4a90d9;            // EPNM accent blue
  --theme-background: #ffffff;        // White background
  --theme-surface: #f5f7fa;           // Light gray surface
  --theme-surface-alt: #e8ecf1;       // Alternate surface for striped rows
  --theme-text-primary: #333333;      // Dark text
  --theme-text-secondary: #666666;    // Secondary text
  --theme-border: #cccccc;            // Border color
  --theme-header-bg: #003366;         // Header background
  --theme-header-text: #ffffff;       // Header text
  --theme-nav-bg: #f0f2f5;           // Navigation background
  --theme-nav-hover: #e0e4ea;        // Navigation hover
  --theme-nav-active: #d0d6e0;       // Navigation active
  --theme-table-header-bg: #003366;  // Table header background
  --theme-table-header-text: #ffffff;// Table header text
  --theme-table-row-hover: #e8f0fe; // Table row hover
  --theme-status-online: #28a745;    // Green status
  --theme-status-offline: #dc3545;   // Red status
  --theme-status-warning: #ffc107;   // Yellow status

  // Layout variables
  --theme-nav-width: 240px;          // Left nav width
  --theme-header-height: 48px;       // Header height
  --theme-font-family: 'Segoe UI', Arial, sans-serif;  // Legacy font stack
  --theme-font-size-base: 13px;      // EPNM uses smaller font
  --theme-border-radius: 2px;        // Minimal border radius (legacy feel)
  --theme-spacing-unit: 4px;         // Tighter spacing
}

// styles/themes/_ems-magnetic.scss
:root[data-theme="magnetic"] {
  // Magnetic/Harbor design system palette
  --theme-primary: #049fd9;           // Cisco/Crosswork teal-blue
  --theme-primary-light: #3eb8e5;
  --theme-primary-dark: #037baa;
  --theme-accent: #6abf4b;            // Cisco green accent
  --theme-background: #1a1a2e;        // Dark background (Magnetic default)
  --theme-surface: #222240;           // Dark surface
  --theme-surface-alt: #2a2a48;
  --theme-text-primary: #ffffff;
  --theme-text-secondary: #b0b0c0;
  --theme-border: #3a3a5c;
  --theme-header-bg: #111128;
  --theme-header-text: #ffffff;
  --theme-nav-bg: #1a1a2e;
  --theme-nav-hover: #2a2a48;
  --theme-nav-active: #3a3a5c;
  --theme-table-header-bg: #222240;
  --theme-table-header-text: #ffffff;
  --theme-table-row-hover: #2a2a48;
  --theme-status-online: #6abf4b;
  --theme-status-offline: #e74c3c;
  --theme-status-warning: #f5a623;

  // Layout variables
  --theme-nav-width: 280px;
  --theme-header-height: 56px;
  --theme-font-family: 'CiscoSans', 'Helvetica Neue', sans-serif;
  --theme-font-size-base: 14px;
  --theme-border-radius: 8px;         // Modern rounded corners
  --theme-spacing-unit: 8px;          // More generous spacing
}
```

**Apply theme variables in component styles:**

```scss
// Shared component styles that respond to the theme
.epnm-data-grid {
  font-family: var(--theme-font-family);
  font-size: var(--theme-font-size-base);
  border: 1px solid var(--theme-border);
  border-radius: var(--theme-border-radius);

  th {
    background-color: var(--theme-table-header-bg);
    color: var(--theme-table-header-text);
    padding: calc(var(--theme-spacing-unit) * 2);
  }

  td {
    padding: calc(var(--theme-spacing-unit) * 2);
    border-bottom: 1px solid var(--theme-border);
    color: var(--theme-text-primary);
  }

  tr:hover {
    background-color: var(--theme-table-row-hover);
  }
}

.epnm-left-nav {
  width: var(--theme-nav-width);
  background-color: var(--theme-nav-bg);
  font-family: var(--theme-font-family);

  .nav-item {
    padding: calc(var(--theme-spacing-unit) * 2) calc(var(--theme-spacing-unit) * 3);
    color: var(--theme-text-primary);

    &:hover {
      background-color: var(--theme-nav-hover);
    }

    &.active {
      background-color: var(--theme-nav-active);
      border-left: 3px solid var(--theme-primary);
    }
  }
}
```

### 7.3 Theme Service

```typescript
// theme.service.ts
import { Injectable, signal, effect } from '@angular/core';

export type ThemeMode = 'classic' | 'magnetic';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  // Signal-based state (Angular 21)
  readonly currentTheme = signal<ThemeMode>('classic');  // EPNM classic is default

  constructor() {
    // Load persisted preference
    const saved = localStorage.getItem('epnm-theme') as ThemeMode | null;
    if (saved) {
      this.currentTheme.set(saved);
    }

    // Apply theme changes to the DOM
    effect(() => {
      const theme = this.currentTheme();
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('epnm-theme', theme);
    });
  }

  toggle(): void {
    this.currentTheme.update(current =>
      current === 'classic' ? 'magnetic' : 'classic'
    );
  }

  isClassic(): boolean {
    return this.currentTheme() === 'classic';
  }
}
```

### 7.4 Toggle Component (Lives in the Shell App Header)

```typescript
// theme-toggle.component.ts
import { Component, inject } from '@angular/core';
import { ThemeService } from '../services/theme.service';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';

@Component({
  selector: 'app-theme-toggle',
  standalone: true,
  imports: [MatSlideToggleModule],
  template: `
    <div class="theme-toggle-container">
      <span class="theme-label">Classic</span>
      <mat-slide-toggle
        [checked]="themeService.currentTheme() === 'magnetic'"
        (change)="themeService.toggle()"
        color="primary">
      </mat-slide-toggle>
      <span class="theme-label">Modern</span>
    </div>
  `,
  styles: [`
    .theme-toggle-container {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .theme-label {
      font-size: 12px;
      color: var(--theme-header-text);
    }
  `]
})
export class ThemeToggleComponent {
  themeService = inject(ThemeService);
}
```

### 7.5 Conditional Component Rendering Based on Theme

Beyond CSS-only theming, some EPNM screens have fundamentally different layouts from EMS screens. For these, the theme toggle should render entirely different components.

```typescript
// inventory-view.component.ts (container component that switches layouts)
import { Component, inject } from '@angular/core';
import { ThemeService } from '../services/theme.service';
import { NetworkDevicesClassicComponent } from './classic/network-devices-classic.component';
import { NetworkDevicesModernComponent } from './modern/network-devices-modern.component';

@Component({
  selector: 'app-inventory-view',
  standalone: true,
  imports: [NetworkDevicesClassicComponent, NetworkDevicesModernComponent],
  template: `
    @if (themeService.currentTheme() === 'classic') {
      <app-network-devices-classic />
    } @else {
      <app-network-devices-modern />
    }
  `
})
export class InventoryViewComponent {
  themeService = inject(ThemeService);
}
```

### 7.6 Theming Decision Matrix

| Scenario | Approach |
|---|---|
| Same layout, different colors/fonts | CSS custom properties only -- single component, theme variables handle the visual difference |
| Same layout, minor structural differences | CSS custom properties + conditional `@if` blocks within the template |
| Fundamentally different layouts | Two separate components (classic + modern), container switches between them based on theme |
| Navigation structure differs | Two navigation components, shell app switches between them |
| Third-party components (Magnetic library) | Use `panelClass` or `::ng-deep` with theme-scoped selectors to override Magnetic defaults in classic mode |

---

## 8. API Integration

### 8.1 The Architecture

The classic view does NOT call the old EPNM backend. It calls the same EMS REST APIs that the modern Magnetic UI calls. The difference is purely in how the response data is presented.

```
                    +-------------------+
                    |  EMS REST APIs    |
                    |  (Spring Boot/Go) |
                    |  (PostgreSQL)     |
                    +--------+----------+
                             |
                    +--------+----------+
                    |  Angular Services |
                    |  (HttpClient)     |
                    +---+----------+----+
                        |          |
              +---------+--+  +----+---------+
              | Classic    |  | Modern       |
              | Components |  | Components   |
              | (EPNM UX) |  | (Magnetic UX)|
              +------------+  +--------------+
```

### 8.2 Shared Service Pattern

Both classic and modern views share the same Angular service layer. The service handles API communication; the components handle presentation.

```typescript
// services/inventory.service.ts (shared by both classic and modern views)
import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, map } from 'rxjs';

// Raw API response model (matches EMS backend response shape)
export interface DeviceApiResponse {
  id: number;
  hostname: string;
  ipAddress: string;
  managementStatus: string;   // "MANAGED" | "UNMANAGED" | "MAINTENANCE"
  deviceFamily: string;       // "CISCO_ASR_9000" | "CISCO_NEXUS_9000" etc.
  softwareVersion: string;
  lastInventoryCollection: string;  // ISO 8601 timestamp
  chassisSerialNumber: string;
  location: {
    site: string;
    building: string;
    floor: string;
  };
}

@Injectable({ providedIn: 'root' })
export class InventoryService {
  private http = inject(HttpClient);
  private baseUrl = '/api/ems/v1/inventory/devices';

  getNetworkDevices(params?: {
    deviceFamily?: string;
    status?: string;
    site?: string;
    page?: number;
    pageSize?: number;
    sortBy?: string;
    sortOrder?: 'asc' | 'desc';
  }): Observable<DeviceApiResponse[]> {
    let httpParams = new HttpParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined) {
          httpParams = httpParams.set(key, String(value));
        }
      });
    }
    return this.http.get<DeviceApiResponse[]>(this.baseUrl, { params: httpParams });
  }

  getDeviceDetails(deviceId: number): Observable<DeviceApiResponse> {
    return this.http.get<DeviceApiResponse>(`${this.baseUrl}/${deviceId}`);
  }

  getDevice360(deviceId: number): Observable<Device360Response> {
    return this.http.get<Device360Response>(`${this.baseUrl}/${deviceId}/360`);
  }

  getChassisView(deviceId: number): Observable<ChassisViewResponse> {
    return this.http.get<ChassisViewResponse>(`${this.baseUrl}/${deviceId}/chassis`);
  }
}
```

### 8.3 Data Transformation for Classic View

The classic view may need to transform EMS API response data to match EPNM's display conventions. This transformation happens in the classic view components or in optional adapter services, NOT in the shared base service.

```typescript
// classic/adapters/epnm-display.adapter.ts
// Transforms EMS API responses to EPNM display format

export class EpnmDisplayAdapter {

  // EMS uses "MANAGED" / "UNMANAGED" / "MAINTENANCE"
  // EPNM displayed "Managed" / "Unmanaged" / "In Maintenance"
  static formatStatus(emsStatus: string): string {
    const statusMap: Record<string, string> = {
      'MANAGED': 'Managed',
      'UNMANAGED': 'Unmanaged',
      'MAINTENANCE': 'In Maintenance',
      'PARTIALLY_MANAGED': 'Partially Managed'
    };
    return statusMap[emsStatus] || emsStatus;
  }

  // EMS uses "CISCO_ASR_9000" enum format
  // EPNM displayed "Cisco ASR 9000 Series"
  static formatDeviceFamily(emsFamily: string): string {
    const familyMap: Record<string, string> = {
      'CISCO_ASR_9000': 'Cisco ASR 9000 Series',
      'CISCO_NEXUS_9000': 'Cisco Nexus 9000 Series',
      'CISCO_NCS_5500': 'Cisco NCS 5500 Series',
      'CISCO_NCS_540': 'Cisco NCS 540 Series'
    };
    return familyMap[emsFamily] || emsFamily.replace(/_/g, ' ');
  }

  // EMS returns ISO 8601 timestamps
  // EPNM displayed "Mar 25, 2026 14:30:22 PDT"
  static formatTimestamp(isoTimestamp: string): string {
    const date = new Date(isoTimestamp);
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      timeZoneName: 'short'
    });
  }
}
```

```typescript
// Usage in classic view component
import { EpnmDisplayAdapter } from '../adapters/epnm-display.adapter';

export class NetworkDevicesClassicComponent implements OnInit {
  private inventoryService = inject(InventoryService);

  displayDevices: ClassicDeviceRow[] = [];

  ngOnInit(): void {
    this.inventoryService.getNetworkDevices().subscribe(apiDevices => {
      // Transform API response to classic display format
      this.displayDevices = apiDevices.map(device => ({
        id: device.id,
        hostname: device.hostname,
        ipAddress: device.ipAddress,
        status: EpnmDisplayAdapter.formatStatus(device.managementStatus),
        deviceType: EpnmDisplayAdapter.formatDeviceFamily(device.deviceFamily),
        softwareVersion: device.softwareVersion,
        lastCollected: EpnmDisplayAdapter.formatTimestamp(device.lastInventoryCollection),
        location: `${device.location.site} / ${device.location.building}`
      }));
    });
  }
}
```

### 8.4 API Response Differences to Watch For

When the classic view consumes EMS APIs, watch for these potential gaps between what EPNM showed and what EMS APIs return:

| EPNM Feature | EMS API Expectation | Gap Risk |
|---|---|---|
| Device count in left filter panel | API must return faceted counts by device type, location | Check if EMS API supports aggregation queries |
| Chassis view images | Bundled as application assets in EMS (confirmed in meeting) | Low risk -- already available |
| Device 360 alarm count badge | API must return alarm count per device | Check if EMS device endpoint includes alarm summary |
| Export device (CSV) | API must support export format or client-side generation | Check if EMS has export endpoint |
| Bulk import (CSV) | API must accept multipart file upload | Check if EMS has import endpoint |
| OEM commands execution | API must support command dispatch to devices | Likely in the ~20% gap -- verify |
| Scheduling (maintain/managed state) | API must support scheduled state transitions | May need new backend endpoints |

---

## 9. Shell App Integration

### 9.1 Current EMS Shell Architecture

From Set 07, the EMS application uses a nested shell architecture:

```
Infra UI (Shell App - outermost)
  |-- Header bar, top navigation, login
  |-- Common UI (shared component library)
  |     |-- Cards, tables, design system widgets
  |     |-- Harbor/Magnetic component implementations
  |
  |-- EMS UI (feature pages - loaded into shell content area)
        |-- Inventory views
        |-- Fault management views
        |-- Software image management
        |-- etc.
```

### 9.2 Where the Toggle Lives

The theme toggle button should live in the **Infra UI** shell header. This is the persistent, always-visible part of the application. The toggle controls a global theme state that all nested layers respond to.

```typescript
// In the Infra UI shell component (header area)
// This is a modification to existing Infra UI code

// app-header.component.ts (existing shell header -- add toggle)
import { ThemeToggleComponent } from './theme-toggle/theme-toggle.component';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [ThemeToggleComponent, /* existing imports */],
  template: `
    <header class="shell-header">
      <div class="header-left">
        <img src="assets/cisco-logo.svg" class="logo" />
        <span class="product-name">Crosswork Network Controller</span>
      </div>
      <div class="header-center">
        <!-- existing navigation -->
      </div>
      <div class="header-right">
        <!-- NEW: Theme toggle added here -->
        <app-theme-toggle />
        <!-- existing user menu, settings, etc. -->
      </div>
    </header>
  `
})
export class AppHeaderComponent { }
```

### 9.3 Classic View Routing Strategy

There are two architectural approaches for how classic view components integrate with the existing EMS routing:

**Option A: Dual routes (separate paths for classic and modern)**

```typescript
// app.routes.ts
const routes: Routes = [
  {
    path: 'inventory/network-devices',
    component: InventoryViewComponent,  // container that switches based on theme
    children: []
  },
  {
    path: 'faults/alarms',
    component: FaultViewComponent,      // container that switches based on theme
    children: []
  }
];
```

In this approach, the URL stays the same regardless of theme. The container component (see Section 7.5) decides which inner component to render based on the `ThemeService` signal.

**Option B: Route guards with theme-aware loading**

```typescript
// classic-view.guard.ts
import { inject } from '@angular/core';
import { CanMatchFn } from '@angular/router';
import { ThemeService } from '../services/theme.service';

export const classicViewGuard: CanMatchFn = () => {
  return inject(ThemeService).currentTheme() === 'classic';
};

export const modernViewGuard: CanMatchFn = () => {
  return inject(ThemeService).currentTheme() === 'magnetic';
};

// app.routes.ts
const routes: Routes = [
  {
    path: 'inventory/network-devices',
    canMatch: [classicViewGuard],
    loadComponent: () => import('./classic/network-devices-classic.component')
      .then(m => m.NetworkDevicesClassicComponent)
  },
  {
    path: 'inventory/network-devices',
    canMatch: [modernViewGuard],
    loadComponent: () => import('./modern/network-devices-modern.component')
      .then(m => m.NetworkDevicesModernComponent)
  }
];
```

**Recommendation:** Option A (container component) is simpler and avoids route re-evaluation on theme toggle. Option B is cleaner for code splitting but requires navigation to trigger route re-matching. For the POC, Option A is the safer choice. If the team is already using `canMatch` patterns in the existing EMS routes, Option B fits the existing architecture better.

### 9.4 Classic View Module Organization

Proposed folder structure within the EMS UI repository:

```
ems-ui/
  src/
    app/
      classic/                          # <-- NEW: All classic view code
        components/
          network-devices-classic/
            network-devices-classic.component.ts
            network-devices-classic.component.html
            network-devices-classic.component.scss
          device-360-classic/
            device-360-classic.component.ts
            device-360-classic.component.html
            device-360-classic.component.scss
          device-details-classic/
            device-details-classic.component.ts
            device-details-classic.component.html
            device-details-classic.component.scss
          chassis-view-classic/
            chassis-view-classic.component.ts
            chassis-view-classic.component.html
            chassis-view-classic.component.scss
          alarm-list-classic/
            alarm-list-classic.component.ts
            alarm-list-classic.component.html
            alarm-list-classic.component.scss
        adapters/
          epnm-display.adapter.ts       # Data transformation for classic display
        styles/
          _epnm-classic.scss            # EPNM theme variables
          _epnm-components.scss         # EPNM-specific component overrides
          _epnm-layout.scss             # EPNM left-nav + content layout
        shared/
          epnm-left-nav/                # Classic left navigation component
          epnm-toolbar/                 # Classic toolbar with action buttons
          epnm-filter-panel/            # Left-side filtering panel
      modern/                           # Existing Magnetic/Harbor components
        components/
          ...
      shared/                           # Shared between classic and modern
        services/
          inventory.service.ts          # API calls (shared)
          alarm.service.ts              # API calls (shared)
          theme.service.ts              # Theme toggle state
          event-bus.service.ts          # Cross-component events
        models/
          network-device.model.ts
          alarm.model.ts
          device-360.model.ts
        containers/
          inventory-view.component.ts   # Switches classic/modern
          fault-view.component.ts       # Switches classic/modern
```

### 9.5 Common UI Reuse

The Common UI repository contains shared components (cards, tables, design system widgets). The classic view should:

1. **Reuse Common UI structural components** where they can be themed via CSS custom properties (e.g., card containers, layout grids)
2. **NOT reuse Common UI components** that are tightly coupled to the Magnetic design system (e.g., Magnetic-specific button styles, Harbor typography)
3. **Create classic-specific wrapper components** that use the same underlying data patterns but apply EPNM-specific styling

Example: If Common UI has a `<cx-data-table>` component that is heavily styled with Magnetic tokens, the classic view should use `<mat-table>` directly with EPNM styling instead of trying to override the Common UI component.

### 9.6 Build Integration

The classic view code must be part of the EMS build pipeline (confirmed requirement from the meeting: "It has to be part of the new EMS build"). This means:

```typescript
// The classic components must be importable from the EMS UI module
// If using lazy loading:
const routes: Routes = [
  {
    path: 'inventory',
    loadChildren: () => import('./classic/classic.routes')
      .then(m => m.CLASSIC_ROUTES)
  }
];
```

The classic view code ships in the same build artifact as the modern EMS UI. There is no separate deployment.

---

## 10. Quick Reference: Complete Migration Checklist per Screen

For each EPNM screen being converted, follow this checklist:

### Step 1: Analyze the EPNM Screen
- [ ] Identify all Dojo widgets used (DataGrid, Dialog, Tree, form widgets)
- [ ] Document the data flow (what API/store does it call?)
- [ ] Map the layout structure (BorderContainer, ContentPane, TabContainer)
- [ ] Note all user interactions (click handlers, context menus, keyboard shortcuts)
- [ ] Capture the visual design (colors, fonts, spacing, borders)

### Step 2: Identify the EMS API Endpoints
- [ ] Find the equivalent EMS REST API for each data source
- [ ] Compare the EPNM data fields with EMS API response fields
- [ ] Document any gaps (fields present in EPNM but absent from EMS API)
- [ ] Note any data format differences requiring adapter transformation

### Step 3: Create the Angular Component
- [ ] Map Dojo widgets to Angular Material components (Section 1)
- [ ] Convert AMD modules to ES6 imports (Section 2)
- [ ] Replace Dojo data binding with Angular binding patterns (Section 3)
- [ ] Replace Dojo event handling with Angular patterns (Section 4)
- [ ] Map lifecycle methods (Section 5)
- [ ] Create/reuse Angular services for state management (Section 6)

### Step 4: Apply EPNM Theming
- [ ] Use CSS custom properties for theme-responsive styling (Section 7)
- [ ] Apply EPNM-specific class names for structural differences
- [ ] Test that the component renders correctly in both classic and modern themes

### Step 5: Integrate with Shell App
- [ ] Add component to the appropriate routing configuration
- [ ] Wire up the theme-switching container component (Section 9.3)
- [ ] Verify component renders within the Infra UI shell
- [ ] Test toggle between classic and modern views

---

## Sources

### Dojo Reference
- [dojox.grid.DataGrid Reference](https://dojotoolkit.org/reference-guide/1.10/dojox/grid/DataGrid.html)
- [Working with the Grid Tutorial](https://dojotoolkit.org/documentation/tutorials/1.10/working_grid/index.html)
- [dijit/Dialog Reference](https://dojotoolkit.org/reference-guide/1.10/dijit/Dialog.html)
- [dijit/Tree ObjectStoreModel](https://dojotoolkit.org/reference-guide/1.10/dijit/tree/ObjectStoreModel.html)
- [Connecting a Store to a Tree](https://dojotoolkit.org/documentation/tutorials/1.10/store_driven_tree/index.html)
- [Understanding _WidgetBase](https://dojotoolkit.org/documentation/tutorials/1.10/understanding_widgetbase/)
- [Dojo Widget Lifecycle](https://justinchmura.com/2015/02/28/dojo-widget-lifecycle/)
- [dojo/Stateful Reference](https://dojotoolkit.org/reference-guide/1.10/dojo/Stateful.html)
- [dojo/topic Reference](https://dojotoolkit.org/reference-guide/1.10/dojo/topic.html)
- [dojo/on Reference](https://dojotoolkit.org/reference-guide/1.10/dojo/on.html)
- [dojo/store Reference](https://dojotoolkit.org/reference-guide/1.10/dojo/store.html)
- [dojo/store/Observable Reference](https://dojotoolkit.org/reference-guide/1.7/dojo/store/Observable.html)
- [Dojo Object Stores (SitePen)](https://www.sitepen.com/blog/dojo-object-stores)
- [dijit Form Widgets Reference](https://dojotoolkit.org/reference-guide/1.8/dijit/form.html)
- [Creating Template-based Widgets](https://dojotoolkit.org/documentation/tutorials/1.10/templated/)
- [Events with Dojo Tutorial](https://dojotoolkit.org/documentation/tutorials/1.10/events/)
- [dojo/aspect vs dojo/on FAQ (SitePen)](https://www.sitepen.com/blog/dojo-faq-what-is-the-difference-between-dojoon-and-dojoaspect)
- [AMD Modules Introduction](https://dojotoolkit.org/documentation/tutorials/1.10/modules/index.html)
- [dgrid Column Definitions](https://dgrid.io/tutorials/0.4/defining_grid_structures/)

### Angular Reference
- [Angular Component Lifecycle](https://angular.dev/guide/components/lifecycle)
- [Angular Two-way Binding](https://angular.dev/guide/templates/two-way-binding)
- [Angular Reactive Forms](https://angular.dev/guide/forms/reactive-forms)
- [Angular Signal Components Guide](https://blog.angular-university.io/angular-signal-components/)
- [Angular Signal Inputs Guide](https://blog.angular-university.io/angular-signal-inputs/)
- [Angular Signals Overview](https://angular.dev/guide/signals)
- [Angular Material Table Guide](https://blog.angular-university.io/angular-material-data-table/)
- [Angular Material Dialog Overview](https://material.angular.dev/components/dialog/overview)
- [Angular CDK Tree](https://material.angular.dev/cdk/tree)
- [Angular Material Dialog Guide](https://blog.angular-university.io/angular-material-dialog/)
- [Angular @HostListener API](https://angular.dev/api/core/HostListener)

### Theming Reference
- [Modern Theming in Angular 20: Light & Dark Mode with Material Design 3](https://trailheadtechnology.com/modern-theming-in-angular-20-light-dark-mode-with-material-design-3/)
- [Theming Angular Apps with CSS Custom Properties](https://coryrylan.com/blog/theming-angular-apps-with-css-custom-properties)
- [Theming System with Angular and CSS Custom Properties](https://developapa.com/angular-theming/)
- [Angular Theme Switcher](https://medium.com/@davdifr/theme-switcher-in-angular-from-dark-to-light-and-back-again-f42fc3f9fab0)

### State Management Reference
- [Angular State Management with BehaviorSubject](https://dev.to/ngconf/angular-state-management-with-behaviorsubject-22b0)
- [Simple State Management in Angular with RxJS](https://dev.to/angular/simple-yet-powerful-state-management-in-angular-with-rxjs-4f8g)
- [Angular HttpClient + Spring Boot REST API](https://www.netjstech.com/2021/01/angulat-httpclient-communicate-with-backend-service.html)
- [Building a Web Application with Spring Boot and Angular (Baeldung)](https://www.baeldung.com/spring-boot-angular-web)

### Migration Tools
- [amd-to-es6 npm package](https://www.npmjs.com/package/amd-to-es6)
- [Migrating AMD Modules to ES6](https://forum.espocrm.com/forum/developer-help/developer-tutorials/95324-migrating-front-end-amd-require-js-modules-to-ecmascript6-es6-classes)
- [Converting Dojo-AMD Projects to TypeScript](https://gis.utah.gov/blog/2016-03-28-converting-dojo-amd-projects-to-type-script/)

### Angular Architecture Reference
- [Feature Flags in Angular](https://sreyaj.dev/implementing-feature-flags-in-angular)
- [Micro-frontends with Angular Module Federation](https://module-federation.io/practice/frameworks/angular/angular-mfe)
- [EventEmitter vs RxJS Subjects in Angular](https://medium.com/@ignatovich.dm/event-emitters-vs-rxjs-subjects-in-angular-choosing-the-right-tool-db241fe1c847)

### Cisco Design System
- [Magnetic Design System GitHub](https://github.com/cisco-magnetic)
- [Cisco Unifying GUIs with Magnetic (The Register)](https://www.theregister.com/2022/12/07/cisco_magnetic_consistent_security_ui/)
- [Cisco EPNM DevNet](https://developer.cisco.com/site/epnm/)
