
# Threading-Multiprocessing

## Threading in Python: Best Practices for Safe and Efficient Concurrency

Python's `threading` module enables concurrent execution of I/O-bound tasks like database access, API calls, and file I/O. This section outlines how to safely use threading in real-world Python applications, especially in Flask-based APIs or backend services.

---

### ✅ When to Use Threading

- Performing multiple **independent DB or network calls**
- Parallelizing API requests or background lookups
- Improving latency in I/O-heavy endpoints

> ⚠️ Threading in Python is best suited for **I/O-bound** operations, not CPU-bound tasks (due to the Global Interpreter Lock — GIL).

---

### ⚠️ Things to Be Careful About

#### 1. One DB Connection Per Thread

- Never share DB connections or cursors across threads.
- Always create and release connections inside the thread.
- Wrap all DB operations in `try/except` to handle failures gracefully.

---

#### 2. Use Locks with Shared In-Memory Data

- When multiple threads read/write shared structures like `dict`, `list`, or in-memory caches, use locks.
- Without locks, you risk data races and inconsistent states.

---

#### 3. Do Not Use Flask Globals Inside Threads

- Flask objects like `request`, `session`, or `g` are not safe to use in background threads.
- Extract all necessary request data before spawning a thread.

---

#### 4. Manage Thread Lifecycles Properly

- Always wait for thread completion using `.join()` or future `.result()`.
- Use `ThreadPoolExecutor` to avoid manual thread management.
- Never spawn threads without proper control or tracking.

---

#### 5. Limit Number of Threads

- Avoid creating too many threads; it can exhaust system resources.
- A safe range is usually **4–10 threads** for I/O-bound workloads.

---

#### 6. Guard Against Race Conditions

- Logic like checking and updating shared state should be protected with locks.
- Even simple read-modify-write patterns can fail without synchronization.

---

#### 7. Understand the Global Interpreter Lock (GIL)

- Python threads do **not run in parallel** for CPU-heavy code.
- Use `multiprocessing` (covered later) for parallel CPU processing.

---

#### 8. Logging and Debugging

- Use thread names and logging context to identify and debug concurrent execution issues.
