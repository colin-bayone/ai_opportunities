# Channels & WebSockets Best Practices

Django Channels with channels-redis for WebSocket support based on your stack.

## Channels Configuration

### Channel Layer Setup
- [ ] `channels` and `channels-redis` installed
- [ ] Channel layer configured in settings
- [ ] Dedicated Redis DB for Channels (e.g., DB 3)
- [ ] Capacity and expiry configured appropriately
- [ ] Channel layer tested before deployment

### ASGI Configuration
- [ ] ASGI application configured in `asgi.py`
- [ ] Protocol routing defined (HTTP + WebSocket)
- [ ] Middleware stack applied to HTTP
- [ ] WebSocket routing separate from HTTP routing
- [ ] ASGI server configured (Uvicorn in development)

### Settings Validation
- [ ] `CHANNEL_LAYERS` dictionary in settings
- [ ] Redis host, port, and DB number correct
- [ ] Capacity set appropriately (default 1500)
- [ ] Expiry set for message timeout (default 10 seconds)
- [ ] Connection parameters valid

## Consumers

### Consumer Types
- [ ] Async consumers for WebSocket (preferred)
- [ ] `AsyncWebsocketConsumer` base class used
- [ ] Sync consumers only when necessary (database-heavy operations)
- [ ] No blocking operations in async consumers

### Consumer Methods
- [ ] `connect()` - Validates connection, accepts/rejects
- [ ] `disconnect()` - Cleanup on disconnect
- [ ] `receive()` - Handles incoming messages
- [ ] Message type handlers for group messages
- [ ] Error handling in all methods

### Connection Handling
- [ ] Authentication checked in `connect()`
- [ ] User available via `self.scope['user']`
- [ ] Session data available via `self.scope['session']`
- [ ] Client group validated if multi-tenant
- [ ] `await self.accept()` called to accept connection
- [ ] `await self.close()` used to reject or close connection

## Authentication

### WebSocket Authentication
- [ ] Session authentication works with WebSockets
- [ ] User authenticated before accept
- [ ] Anonymous users handled appropriately
- [ ] Token authentication if using (query param or initial message)
- [ ] No authentication bypass for WebSocket connections

### Session Access
- [ ] Session middleware in ASGI stack
- [ ] Session data accessible in consumer
- [ ] Client group from session validated
- [ ] Session mutations saved if needed

## Channel Groups

### Group Management
- [ ] Groups used for broadcasting to multiple consumers
- [ ] Group names follow naming convention: `chat_room_{id}`
- [ ] Consumers join groups in `connect()` 
- [ ] Consumers leave groups in `disconnect()`
- [ ] No memory leaks (always discard from group)

### Group Operations
- [ ] `await self.channel_layer.group_add(group, channel)` - Join group
- [ ] `await self.channel_layer.group_discard(group, channel)` - Leave group
- [ ] `await self.channel_layer.group_send(group, message)` - Send to group
- [ ] Group names validated and sanitized
- [ ] No infinite loops in group messaging

## Message Handling

### Message Format
- [ ] Messages are dictionaries
- [ ] `type` key specifies handler method
- [ ] Handler method name: snake_case version of type
- [ ] Additional keys contain message data
- [ ] Message structure consistent across application

### Message Types
- [ ] Type handlers defined: `async def chat_message(self, event)`
- [ ] Type corresponds to method: `chat.message` → `chat_message()`
- [ ] Handler sends to WebSocket: `await self.send()`
- [ ] Error handling in type handlers
- [ ] No unhandled message types

### Sending Messages
- [ ] `await self.send(text_data=json.dumps(data))` for text
- [ ] `await self.send(bytes_data=data)` for binary
- [ ] Messages serialized to JSON
- [ ] No unserializable data (use strings, numbers, lists, dicts)
- [ ] Large messages chunked if necessary

## Routing

### WebSocket Routing
- [ ] WebSocket routes in routing configuration
- [ ] URL patterns use `path()` or `re_path()`
- [ ] Consumers mapped to paths
- [ ] URL parameters accessible via `self.scope['url_route']['kwargs']`
- [ ] No conflicting routes

### Protocol Router
- [ ] `ProtocolTypeRouter` routes by protocol (http, websocket)
- [ ] HTTP routes to Django ASGI application
- [ ] WebSocket routes to custom routing
- [ ] All protocols handled

## Real-Time Features

### Streaming Responses
- [ ] Streaming chat with Azure OpenAI
- [ ] Chunks sent immediately to WebSocket
- [ ] Progress updates for long operations
- [ ] Task status updates via WebSocket
- [ ] Connection kept alive during streaming

### Live Updates
- [ ] Notifications pushed via WebSocket
- [ ] System monitoring live updates
- [ ] Log tails streamed in real-time
- [ ] Collaborative editing updates
- [ ] No polling (WebSocket replaces polling)

## Integration with Django

### Triggering WebSocket Messages
- [ ] Use `get_channel_layer()` to access channel layer
- [ ] `async_to_sync()` wrapper for sync code
- [ ] Send to specific channel or group
- [ ] Message format matches consumer expectations
- [ ] Error handling when sending fails

### From Views
- [ ] Views can trigger WebSocket messages
- [ ] Use channel layer to send to group
- [ ] Notify connected clients of updates
- [ ] No direct WebSocket access from views

### From Celery Tasks
- [ ] Celery tasks can send WebSocket messages
- [ ] Use `async_to_sync(channel_layer.group_send())`
- [ ] Notify clients of task completion
- [ ] Progress updates during task execution

## Error Handling

### Consumer Errors
- [ ] Try-except in consumer methods
- [ ] Log errors with context
- [ ] Send error message to client
- [ ] Close connection on fatal errors
- [ ] No unhandled exceptions

### Connection Errors
- [ ] Handle disconnect gracefully
- [ ] Clean up resources on disconnect
- [ ] Retry logic on client side if needed
- [ ] Exponential backoff for reconnection
- [ ] Alert on repeated connection failures

### Message Parsing Errors
- [ ] Validate incoming messages
- [ ] JSON parsing errors caught
- [ ] Send error response to client
- [ ] Log malformed messages
- [ ] No crashes from invalid input

## Security

### Input Validation
- [ ] All incoming messages validated
- [ ] JSON schema validation if complex
- [ ] Sanitize user input
- [ ] Rate limiting on WebSocket messages
- [ ] No SQL injection via WebSocket data

### Authorization
- [ ] Permissions checked before sending data
- [ ] Client group boundaries enforced
- [ ] No cross-tenant data leakage
- [ ] Admin-only features protected
- [ ] User can only access their own data

### Origin Checking
- [ ] Allowed origins configured
- [ ] CORS settings for WebSocket
- [ ] Reject connections from unknown origins
- [ ] Production origin list maintained

## Performance

### Connection Management
- [ ] Connections closed when no longer needed
- [ ] Idle timeout configured
- [ ] Maximum connection limit considered
- [ ] Connection pooling for Redis
- [ ] No connection leaks

### Message Efficiency
- [ ] Small, focused messages
- [ ] Binary format for large data
- [ ] Compression if beneficial
- [ ] Batching multiple updates when appropriate
- [ ] No excessive message frequency

### Scaling
- [ ] Multiple workers can handle WebSocket connections
- [ ] Redis channel layer scales horizontally
- [ ] Sticky sessions if needed
- [ ] Load balancing WebSocket connections
- [ ] Monitor connection count per worker

## Testing

### Consumer Testing
- [ ] Use `WebsocketCommunicator` for testing
- [ ] Test connect/disconnect flow
- [ ] Test message receiving
- [ ] Test message sending to groups
- [ ] Test authentication and authorization

### Integration Testing
- [ ] Test with real Redis in integration tests
- [ ] Test full WebSocket lifecycle
- [ ] Test concurrent connections
- [ ] Test error scenarios
- [ ] Test reconnection logic

## Monitoring

### Connection Metrics
- [ ] Track active connections
- [ ] Monitor connection duration
- [ ] Alert on connection spikes
- [ ] Track connection failures
- [ ] Monitor by consumer type

### Message Metrics
- [ ] Track message rate (sent/received)
- [ ] Monitor message latency
- [ ] Track failed messages
- [ ] Alert on message backlog
- [ ] Monitor Redis channel layer health

## Common Patterns

### Chat Application
- [ ] User joins room (group)
- [ ] Messages broadcast to room group
- [ ] User leaves room on disconnect
- [ ] History loaded from database
- [ ] Presence indicators (who's online)

### Notifications
- [ ] User-specific notification channel
- [ ] System-wide broadcast channel
- [ ] Notification persistence in database
- [ ] Mark as read via WebSocket
- [ ] Toast/popup in UI

### Live Dashboard
- [ ] Real-time metrics updates
- [ ] System status monitoring
- [ ] Auto-refresh without polling
- [ ] Multiple dashboard clients supported
- [ ] Filtered updates by user permissions

### Collaborative Editing
- [ ] Document-specific channel
- [ ] Conflict resolution strategy
- [ ] Operational transforms if needed
- [ ] Save to database periodically
- [ ] Lock mechanism if exclusive editing

## Common Issues

### Connection Refused
- [ ] Check Channels installed and configured
- [ ] Verify Redis running and accessible
- [ ] Check ASGI configuration
- [ ] Verify WebSocket routing
- [ ] Check firewall/network settings

### Messages Not Received
- [ ] Verify group membership
- [ ] Check message type matches handler
- [ ] Verify channel layer configuration
- [ ] Check Redis capacity not exceeded
- [ ] Check message expiry timeout

### Authentication Fails
- [ ] Session middleware in ASGI stack
- [ ] Cookies sent with WebSocket connection
- [ ] Session data accessible in consumer
- [ ] Authentication backend configured
- [ ] No CSRF issues (WebSocket doesn't use CSRF)

### Memory Leaks
- [ ] Consumers always leave groups on disconnect
- [ ] No global state in consumers
- [ ] Close database connections if sync consumer
- [ ] Clear large data structures
- [ ] Monitor memory usage over time

## Deployment

### Production Settings
- [ ] ASGI server configured (Daphne, Uvicorn)
- [ ] Multiple ASGI workers for scaling
- [ ] Redis channel layer in production
- [ ] WebSocket proxy (nginx, etc.) configured
- [ ] SSL/TLS for secure WebSockets (wss://)

### Load Balancing
- [ ] Load balancer supports WebSocket
- [ ] Sticky sessions if needed
- [ ] Health checks for ASGI workers
- [ ] Connection draining on deploy
- [ ] Zero-downtime deployment strategy

## Cross-Reference

Related docs:
- `redis_best_practices.md` - Redis as channel layer
- `azure_openai_best_practices.md` - Streaming responses
- `authentication_authorization_best_practices.md` - WebSocket auth
- `web_security_best_practices.md` - WebSocket security
- `performance_monitoring_best_practices.md` - Connection monitoring
