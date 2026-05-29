use rate_limiter::{TokenBucket, SharedRateLimiter, RateLimiter};
// use std::time::{Duration, Instant};

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
