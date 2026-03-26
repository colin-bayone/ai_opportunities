# PR #1253 Requested Changes

**PR:** #1253
**Issue:** #1241
**Author:** smauryabayonesolutions
**Reviewer:** cmoore
**Date:** 2026-01-26

---

## Requested Changes

### CHANGE-001: Remove "Re:" Prefix Logic from View

**Related Finding:** FINDING-001
**File:** `communications/views/email_simple_views.py`
**Lines:** 149-152

**Current code:**
```python
subject = thread.subject or ''
if subject and not subject.lower().startswith('re:'):
    subject = f"Re: {subject}"
```

**Change to:**
```python
subject = thread.subject or ''
```

**Reason:**
- Inconsistent with `ComposeEmailView` which does not add "Re:" prefix
- The Graph API reply endpoint handles subject formatting automatically
- We should pass what's stored in the database, not add formatting

---

### CHANGE-002: Remove "Re:" Prefix from Template Display

**Related Finding:** FINDING-001 (related)
**File:** `communications/templates/communications/simple_thread_detail.html`
**Lines:** 88-91

**Current code:**
```html
<input type="text"
       class="form-control"
       value="Re: {{ thread.subject }}"
       readonly
       disabled>
```

**Change to:**
```html
<input type="text"
       class="form-control"
       value="{{ thread.subject|default:'' }}"
       readonly
       disabled>
```

**Reason:**
- Display what's stored in the database, not formatted versions
- If the subject already has "Re:" from the conversation, it's already there
- Adding "Re:" on top could result in "Re: Re: Subject" display issues

---

### CHANGE-003: Fix Flaky Test with Explicit received_at Values

**Related Finding:** FINDING-003
**File:** `communications/tests/test_email_simple_views.py`
**Location:** `SimpleThreadDetailViewTests.setUp()` (around line 170)

**Current code:**
```python
# Outbound message
EmailMessage.objects.create(
    graph_message_id='msg-out-1',
    conversation_id='conv-detail-123',
    thread=self.thread,
    sender_email='test@bayone.com',
    ...
)
# Inbound message
EmailMessage.objects.create(
    graph_message_id='msg-in-1',
    conversation_id='conv-detail-123',
    thread=self.thread,
    sender_email='candidate@example.com',
    ...
)
```

**Change to:**
```python
from django.utils import timezone
from datetime import timedelta

# Outbound message - older
EmailMessage.objects.create(
    graph_message_id='msg-out-1',
    conversation_id='conv-detail-123',
    thread=self.thread,
    sender_email='test@bayone.com',
    ...,
    received_at=timezone.now() - timedelta(hours=1)
)
# Inbound message - newer (latest)
EmailMessage.objects.create(
    graph_message_id='msg-in-1',
    conversation_id='conv-detail-123',
    thread=self.thread,
    sender_email='candidate@example.com',
    ...,
    received_at=timezone.now()
)
```

**Reason:**
- View orders by `-received_at` to get latest message
- With NULL values, PostgreSQL ordering is non-deterministic
- Test `test_reply_uses_latest_message_for_threading` could be flaky
- Explicit timestamps ensure deterministic test behavior

---

### CHANGE-004: Move Inline JavaScript to Separate File

**Related Finding:** FINDING-005
**Files:**
- `communications/templates/communications/simple_thread_detail.html` (remove inline JS)
- `communications/static/communications/js/reply-form.js` (create new file)

**Current code in template (lines 116-130):**
```html
<script>
document.getElementById('reply-form').addEventListener('submit', function(e) {
    var body = document.getElementById('body').value.trim();
    if (!body) {
        e.preventDefault();
        alert('Please enter a reply message.');
        document.getElementById('body').focus();
        return false;
    }
    var submitBtn = document.getElementById('send-reply-btn');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
});
</script>
```

**Change to:**

1. Create `communications/static/communications/js/reply-form.js`:
```javascript
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('reply-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            var body = document.getElementById('body').value.trim();
            if (!body) {
                e.preventDefault();
                alert('Please enter a reply message.');
                document.getElementById('body').focus();
                return false;
            }
            var submitBtn = document.getElementById('send-reply-btn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
        });
    }
});
```

2. In template, replace inline script with:
```html
{% block extra_js %}
<script src="{% static 'communications/js/reply-form.js' %}"></script>
{% endblock %}
```

**Reason:**
- Project pattern: JS files go in `app/static/app/js/`
- Inline JavaScript is not accepted
- See `recruitment/candidates/templates/candidates/search/search.html` for reference pattern

---

### CHANGE-005: Use Bootstrap Inline Validation Instead of alert()

**Related Finding:** FINDING-006
**Files:**
- `communications/static/communications/js/reply-form.js` (the new JS file from CHANGE-004)
- `communications/templates/communications/simple_thread_detail.html` (add error feedback div)

**Current validation pattern:**
```javascript
if (!body) {
    e.preventDefault();
    alert('Please enter a reply message.');
    document.getElementById('body').focus();
    return false;
}
```

**Change to match codebase pattern:**

1. In the JS file (`reply-form.js`):
```javascript
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('reply-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            var bodyField = document.getElementById('body');
            var body = bodyField.value.trim();
            var errorDiv = document.getElementById('body-error');

            // Clear previous error state
            bodyField.classList.remove('is-invalid');
            if (errorDiv) errorDiv.style.display = 'none';

            if (!body) {
                e.preventDefault();
                bodyField.classList.add('is-invalid');
                if (errorDiv) {
                    errorDiv.textContent = 'Please enter a reply message.';
                    errorDiv.style.display = 'block';
                }
                bodyField.focus();
                return false;
            }

            // Disable button to prevent double-submit
            var submitBtn = document.getElementById('send-reply-btn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
        });
    }
});
```

2. In the template, add error feedback div below textarea:
```html
<div class="mb-3">
    <label for="body" class="form-label">Message</label>
    <textarea name="body"
              id="body"
              class="form-control"
              rows="6"
              placeholder="Type your reply..."
              required></textarea>
    <div id="body-error" class="invalid-feedback" style="display: none;"></div>
</div>
```

**Reason:**
- `alert()` is not the project standard
- Project uses Bootstrap inline validation (`is-invalid` class + `invalid-feedback` div)
- See `core/accounts/templates/account/signup.html` and `core/accounts/templates/socialaccount/signup.html` for reference pattern

---

### CHANGE-006: Add Edge Case Tests

**Related Finding:** FINDING-007
**File:** `communications/tests/test_email_simple_views.py`

**Add the following tests:**

1. **Test for thread with null subject:**
```python
@patch('integrations.microsoft.email.service.EmailService')
def test_reply_with_null_subject(self, mock_email_service_class):
    """Test reply works when thread.subject is None."""
    thread_no_subject = EmailThread.objects.create(
        thread_id='conv-no-subject',
        initiated_by=self.user,
        candidate_email='test@example.com',
        subject=None,  # Null subject
        is_active=True
    )
    EmailMessage.objects.create(
        graph_message_id='msg-no-subj-1',
        conversation_id='conv-no-subject',
        thread=thread_no_subject,
        sender_email='test@example.com',
        direction='inbound',
        owner=self.user,
        received_at=timezone.now()
    )

    mock_service = MagicMock()
    mock_service.send_to_candidate.return_value = {'success': True}
    mock_email_service_class.return_value = mock_service

    response = self.client.post(
        reverse('communications:simple_thread_detail', args=[thread_no_subject.thread_id]),
        {'body': 'Test reply'}
    )

    self.assertEqual(response.status_code, 302)
    call_kwargs = mock_service.send_to_candidate.call_args[1]
    self.assertEqual(call_kwargs['subject'], '')  # Should be empty string, not "None"
```

**Why this matters:** The view handles null subject with `thread.subject or ''`, but without a test, a future change could break this and cause "None" to appear in emails or the UI.

2. **Test for thread with no messages:**
```python
@patch('integrations.microsoft.email.service.EmailService')
def test_reply_to_thread_with_no_messages(self, mock_email_service_class):
    """Test reply works when thread has no messages (edge case)."""
    empty_thread = EmailThread.objects.create(
        thread_id='conv-empty',
        initiated_by=self.user,
        candidate_email='test@example.com',
        subject='Empty Thread',
        is_active=True
    )
    # No messages created

    mock_service = MagicMock()
    mock_service.send_to_candidate.return_value = {'success': True}
    mock_email_service_class.return_value = mock_service

    response = self.client.post(
        reverse('communications:simple_thread_detail', args=[empty_thread.thread_id]),
        {'body': 'Test reply'}
    )

    self.assertEqual(response.status_code, 302)
    call_kwargs = mock_service.send_to_candidate.call_args[1]
    self.assertIsNone(call_kwargs['message_id'])  # No message to reply to
```

**Why this matters:** The view does `thread.messages.order_by('-received_at').first()` which returns None if no messages exist. The code handles this (`latest_message.graph_message_id if latest_message else None`), but this code path has no test coverage. If someone refactors and removes the None check, tests should catch it.

---
