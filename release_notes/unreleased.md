**Unreleased**

* - Added `block_user` action to block users from accessing storage resources
  * - Supports `user_id`, `user_ips`, and `duration` parameters
  * - Duration options: permanent or timed blocks (1, 2, 4, 8, 12, 24 hours)
  * - Client IPs required for NFS, optional for CIFS/SMB
