"""
Contact glossary management.
Maps names to email addresses for quick person lookup.

Storage: claude/meeting_transcripts/contacts.json

Usage:
    from contacts import ContactsManager

    mgr = ContactsManager()
    email = mgr.lookup("Ambar")              # Case-insensitive search
    mgr.add("Ambar Singh", "ambar@bay.com")  # Save new contact
    all_contacts = mgr.list_all()             # Get everything
"""

import json
import sys
from pathlib import Path


DEFAULT_CONTACTS_PATH = "claude/meeting_transcripts/contacts.json"


class ContactsManager:
    """Manage a name-to-email glossary stored as JSON."""

    def __init__(self, contacts_file: str = None):
        if contacts_file:
            self.path = Path(contacts_file)
        else:
            self.path = Path(DEFAULT_CONTACTS_PATH)
        self.contacts = self._load()

    def _load(self) -> dict:
        """Load contacts from file."""
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except json.JSONDecodeError:
                return {}
        return {}

    def _save(self):
        """Persist contacts to file."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.contacts, indent=2, sort_keys=True))

    def lookup(self, name: str) -> str | None:
        """
        Find email by name (case-insensitive, partial match).

        Returns the email if found, None if not.
        If multiple matches, returns the first one and prints all matches.
        """
        name_lower = name.lower().strip()
        exact_matches = []
        partial_matches = []

        for stored_name, email in self.contacts.items():
            stored_lower = stored_name.lower()
            if stored_lower == name_lower:
                exact_matches.append((stored_name, email))
            elif name_lower in stored_lower or stored_lower in name_lower:
                partial_matches.append((stored_name, email))

        if exact_matches:
            return exact_matches[0][1]

        if len(partial_matches) == 1:
            return partial_matches[0][1]

        if len(partial_matches) > 1:
            print(f"Multiple matches for '{name}':")
            for pname, pemail in partial_matches:
                print(f"  {pname}: {pemail}")
            print("Please be more specific or use the full email address.")
            return None

        return None

    def add(self, name: str, email: str):
        """
        Add a contact. Stores the full name and also stores first name
        as a shortcut if it doesn't conflict with an existing entry.
        """
        email = email.strip().lower()
        name = name.strip()

        self.contacts[name] = email

        # Also store first name as shortcut if unique
        first_name = name.split()[0] if " " in name else None
        if first_name and first_name not in self.contacts:
            self.contacts[first_name] = email

        self._save()
        print(f"Saved contact: {name} -> {email}")

    def remove(self, name: str) -> bool:
        """Remove a contact by name. Returns True if found and removed."""
        if name in self.contacts:
            del self.contacts[name]
            self._save()
            return True
        return False

    def list_all(self) -> dict:
        """Return all contacts."""
        return dict(self.contacts)

    def list_formatted(self) -> str:
        """Return contacts as a formatted string for display."""
        if not self.contacts:
            return "No contacts saved yet."

        # Group by email to show aliases
        email_to_names = {}
        for name, email in sorted(self.contacts.items()):
            if email not in email_to_names:
                email_to_names[email] = []
            email_to_names[email].append(name)

        lines = []
        for email, names in sorted(email_to_names.items()):
            names_str = ", ".join(names)
            lines.append(f"  {names_str} -> {email}")

        return "\n".join(lines)


def main():
    """CLI interface for contacts management."""
    import argparse

    parser = argparse.ArgumentParser(description="Contact glossary management")
    parser.add_argument("--file", help="Path to contacts.json")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--lookup", metavar="NAME", help="Look up a person by name")
    group.add_argument("--add", nargs=2, metavar=("NAME", "EMAIL"), help="Add a contact")
    group.add_argument("--remove", metavar="NAME", help="Remove a contact")
    group.add_argument("--list", action="store_true", help="List all contacts")

    args = parser.parse_args()

    mgr = ContactsManager(contacts_file=args.file)

    if args.lookup:
        email = mgr.lookup(args.lookup)
        if email:
            print(f"{args.lookup} -> {email}")
        else:
            print(f"No contact found for '{args.lookup}'")
            sys.exit(1)

    elif args.add:
        name, email = args.add
        mgr.add(name, email)

    elif args.remove:
        if mgr.remove(args.remove):
            print(f"Removed: {args.remove}")
        else:
            print(f"Contact not found: {args.remove}")
            sys.exit(1)

    elif args.list:
        print(mgr.list_formatted())


if __name__ == "__main__":
    main()
