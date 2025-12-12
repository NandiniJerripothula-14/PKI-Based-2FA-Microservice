#!/usr/bin/env python3
"""Test persistence and cron job functionality."""
import subprocess
import time

def test_persistence():
    """Test that seed persists across container restart."""
    print("=" * 60)
    print("PERSISTENCE TEST")
    print("=" * 60)
    
    # Check seed file exists
    print("\n1. Checking seed in volume...")
    result = subprocess.run(
        ["docker", "exec", "pki-2fa-app", "cat", "/data/seed.txt"],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    if result.returncode == 0 and result.stdout.strip():
        seed_before = result.stdout.strip()
        print(f"✅ Seed found: {seed_before[:32]}...")
    else:
        print(f"❌ Seed not found: {result.stderr}")
        return False
    
    # Restart container
    print("\n2. Restarting container...")
    subprocess.run(["docker", "compose", "restart"], cwd="c:\\Users\\jerri\\PKI-Based-2FA-MicroService")
    time.sleep(5)
    
    # Check seed still exists
    print("\n3. Checking seed after restart...")
    result = subprocess.run(
        ["docker", "exec", "pki-2fa-app", "cat", "/data/seed.txt"],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    if result.returncode == 0 and result.stdout.strip():
        seed_after = result.stdout.strip()
        print(f"✅ Seed found: {seed_after[:32]}...")
        
        if seed_before == seed_after:
            print(f"✅ PERSISTENCE VERIFIED: Seed unchanged after restart")
            return True
        else:
            print(f"❌ PERSISTENCE FAILED: Seed changed after restart")
            return False
    else:
        print(f"❌ Seed not found after restart: {result.stderr}")
        return False

def test_cron_job():
    """Test that cron job is executing."""
    print("\n" + "=" * 60)
    print("CRON JOB TEST")
    print("=" * 60)
    
    print("\nWaiting 75 seconds for cron execution...")
    print("Cron runs every minute, we need to wait for at least 2 cycles")
    
    # Count entries before
    result = subprocess.run(
        ["docker", "exec", "pki-2fa-app", "wc", "-l", "/cron/last_code.txt"],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    lines_before = int(result.stdout.split()[0]) if result.returncode == 0 else 0
    print(f"Cron log lines before wait: {lines_before}")
    
    # Wait for cron to execute
    for i in range(75):
        print(f"\rWaiting... {i}s", end="", flush=True)
        time.sleep(1)
    
    print("\n\nChecking cron log...")
    result = subprocess.run(
        ["docker", "exec", "pki-2fa-app", "cat", "/cron/last_code.txt"],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    if result.returncode == 0 and result.stdout.strip():
        lines_after = len(result.stdout.strip().split('\n'))
        print(f"Cron log lines after wait: {lines_after}")
        
        print("\nLast 3 cron entries:")
        for line in result.stdout.strip().split('\n')[-3:]:
            print(f"  {line}")
        
        if lines_after > lines_before:
            print(f"\n✅ CRON JOB VERIFIED: {lines_after - lines_before} new entries created")
            return True
        else:
            print(f"❌ CRON JOB FAILED: No new entries in log")
            return False
    else:
        print(f"❌ Cron log not found: {result.stderr}")
        return False

def main():
    results = []
    
    results.append(("Persistence across restart", test_persistence()))
    results.append(("Cron job execution", test_cron_job()))
    
    print("\n" + "=" * 60)
    print("PERSISTENCE & CRON RESULTS")
    print("=" * 60)
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(p for _, p in results)
    if all_passed:
        print("\n✅ ALL PERSISTENCE & CRON TESTS PASSED!")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        return 1

if __name__ == '__main__':
    exit(main())
