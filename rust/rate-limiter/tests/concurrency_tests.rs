// tests/concurrency.rs
use rate_limiter::SharedRateLimiter;
use std::sync::Arc;
use std::thread;

#[test]
fn shared_limiter_thread_safety() {
    let limiter = Arc::new(SharedRateLimiter::new(100.0, 50.0));
    let mut handles = vec![];

    // Spawn 4 threads, each trying to acquire 25 tokens
    for _ in 0..4 {
        let lim = Arc::clone(&limiter);
        handles.push(thread::spawn(move || {
            for _ in 0..25 {
                let _ = lim.try_acquire(1);
            }
        }));
    }

    // Wait for all threads to finish
    for h in handles {
        h.join().unwrap();
    }

    // Total tokens consumed <= initial capacity (some may have been denied)
    assert!(limiter.available_tokens() <= 100.0);
}

#[test]
fn shared_limiter_concurrent_burst() {
    let limiter = Arc::new(SharedRateLimiter::new(10.0, 1.0));
    let mut handles = vec![];

    // Try to acquire 1 token from 20 threads simultaneously
    for _ in 0..20 {
        let lim = Arc::clone(&limiter);
        handles.push(thread::spawn(move || {
            lim.try_acquire(1)
        }));
    }

    // Count successes
    let successes: usize = handles
        .into_iter()
        .map(|h| h.join().unwrap().is_ok() as usize)
        .sum();

    // Exactly 10 should succeed (initial capacity)
    assert_eq!(successes, 10);
}
