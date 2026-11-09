# Slurm on the work computer (one-time setup)

Run these on the Mint machine (`elaines`). `sudo` is needed.

```bash
sudo apt install -y slurm-wlm
sudo mkdir -p /etc/slurm /var/spool/slurmctld /var/spool/slurmd /var/log/slurm
sudo chown slurm: /var/spool/slurmctld /var/log/slurm
```

Copy `slurm/work_computer_slurm.conf` from this repo to `/etc/slurm/slurm.conf`
(on the Mac: `scp slurm/work_computer_slurm.conf elaines@<ip>:/tmp/`, then on the
work computer `sudo cp /tmp/work_computer_slurm.conf /etc/slurm/slurm.conf`).

```bash
sudo systemctl enable --now slurmctld slurmd
sinfo            # node "elaines" should be idle
srun hostname    # should print "elaines"
```

If `sinfo` shows the node as `drain` or `down`:

```bash
sudo scontrol update nodename=elaines state=resume
```

The node name must match `hostname` exactly (`elaines`). If the machine's
hostname ever changes, edit `SlurmctldHost` and `NodeName` to match.
