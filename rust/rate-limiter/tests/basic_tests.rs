use rate_limiter::{TokenBucket, SharedRateLimiter, RateLimiter};
use std::time::{Duration, Instant};

#[test]
fn test_basic_rate_limiting_flow() {
    let mut bucket = TokenBucket::new(3.0, 1.0);

    // Burn through 3 tokens
    assert!(bucket.try_acquire(1).is_ok());
    assert!(bucket.try_acquire(1).is_ok());
    assert!(bucket.try_acquire(1).is_ok());

    // This one should fail because the bucket is empty
    let penalty = bucket.try_acquire(1).unwrap_err();
    assert!(penalty.as_secs_f64() > 0.0);
}

#[test]
fn test_thread_safe_limiter() {
    let limiter = SharedRateLimiter::new(10.0, 1.0);
    assert!(limiter.try_acquire(1).is_ok());
}

#[test]
fn basic_burst_and_refill_real_time() {
    let mut bucket = TokenBucket::with_starting_tokens(3.0, 10.0, 3.0); // High rate for fast test

    // Burn through initial capacity
    assert!(bucket.try_acquire(1).is_ok());
    assert!(bucket.try_acquire(1).is_ok());
    assert!(bucket.try_acquire(1).is_ok());

    // Should be denied now
    let wait = bucket.try_acquire(1).unwrap_err();
    assert!(wait.as_secs_f64() > 0.0);

    // Wait for real refill (10 tokens/sec → 0.1s for 1 token)
    std::thread::sleep(Duration::from_millis(150));
    assert!(bucket.try_acquire(1).is_ok());
}

#[test]
fn cost_greater_than_capacity() {
    let mut bucket = TokenBucket::new(5.0, 2.0);
    let wait = bucket.try_acquire(10).unwrap_err();
    assert!(wait.as_secs_f64() > 0.0);
}

#[test]
fn zero_cost_always_succeeds() {
    let mut bucket = TokenBucket::new(1.0, 0.5);
    bucket.try_acquire(1).unwrap(); // Drain it
    assert!(bucket.try_acquire(0).is_ok()); // Zero cost always works
}

#[test]
fn idle_capping_real_time() {
    let mut bucket = TokenBucket::with_starting_tokens(5.0, 100.0, 1.0); // Fast refill
    bucket.try_acquire(1).unwrap(); // Use 1 token

    // Wait long enough to theoretically refill 100+ tokens, but should cap at 5
    std::thread::sleep(Duration::from_millis(100));

    // Should have exactly capacity tokens (within float tolerance)
    assert!((bucket.available_tokens() - 5.0).abs() < 0.1);
}
