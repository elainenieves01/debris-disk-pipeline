import rebound
import numpy as np


def read_orbital_evolution(config):
    archive_name = config["simulation"]["output_file"]
    n_planets = len(config["planets"])
    npl = int(config["dwarf_planets"]["N"])
    Npart = int(config["test_particles"]["N"])

    sa = rebound.Simulationarchive(archive_name)

    Nsnap = len(sa)
    times = np.zeros(Nsnap)

    aGP = np.full((Nsnap, n_planets), np.nan)
    eGP = np.full((Nsnap, n_planets), np.nan)
    iGP = np.full((Nsnap, n_planets), np.nan)

    sfdps = np.full(Nsnap, np.nan)
    sfps = np.full(Nsnap, np.nan)

    adps = np.full((Nsnap, npl), np.nan)
    edps = np.full((Nsnap, npl), np.nan)
    idps = np.full((Nsnap, npl), np.nan)
    mdps = np.full((Nsnap, npl), np.nan)

    aps = np.full((Nsnap, Npart), np.nan)
    eps = np.full((Nsnap, Npart), np.nan)
    ips = np.full((Nsnap, Npart), np.nan)

    for i, sim_i in enumerate(sa):
        times[i] = sim_i.t

        for j in range(min(n_planets, sim_i.N_active - 1)):
            p = sim_i.particles[1 + j]
            aGP[i, j] = p.a
            eGP[i, j] = p.e
            iGP[i, j] = np.rad2deg(p.inc)

        current_npl = sim_i.N_active - 1 - n_planets
        current_Npart = sim_i.N - sim_i.N_active

        sfdps[i] = current_npl / npl if npl > 0 else np.nan
        sfps[i] = current_Npart / Npart if Npart > 0 else np.nan

        for j in range(min(current_Npart, Npart)):
            p = sim_i.particles[j + sim_i.N_active]
            aps[i, j] = p.a
            eps[i, j] = p.e
            ips[i, j] = np.rad2deg(p.inc)

        for k in range(min(current_npl, npl)):
            p = sim_i.particles[k + 1 + n_planets]
            adps[i, k] = p.a
            edps[i, k] = p.e
            idps[i, k] = np.rad2deg(p.inc)
            mdps[i, k] = p.m

    stats = {}

    stats["aps_means"] = np.nanmean(aps, axis=1)
    stats["eps_means"] = np.nanmean(eps, axis=1)
    stats["ips_means"] = np.nanmean(ips, axis=1)

    stats["aps_median"] = np.nanmedian(aps, axis=1)
    stats["eps_median"] = np.nanmedian(eps, axis=1)
    stats["ips_median"] = np.nanmedian(ips, axis=1)

    stats["adps_means"] = np.nanmean(adps, axis=1)
    stats["edps_means"] = np.nanmean(edps, axis=1)
    stats["idps_means"] = np.nanmean(idps, axis=1)

    stats["adps_median"] = np.nanmedian(adps, axis=1)
    stats["edps_median"] = np.nanmedian(edps, axis=1)
    stats["idps_median"] = np.nanmedian(idps, axis=1)

    stats["eps_rms"] = np.sqrt(np.nanmean(eps**2, axis=1))
    stats["ips_rms"] = np.sqrt(np.nanmean(ips**2, axis=1))

    stats["edps_rms"] = np.sqrt(np.nanmean(edps**2, axis=1))
    stats["idps_rms"] = np.sqrt(np.nanmean(idps**2, axis=1))

    stats["eall_rms"] = np.sqrt(
        np.nanmean(np.concatenate([eps, edps], axis=1)**2, axis=1)
    )

    stats["iall_rms"] = np.sqrt(
        np.nanmean(np.concatenate([ips, idps], axis=1)**2, axis=1)
    )

    data = {
        "times": times,
        "n_planets": n_planets,
        "aGP": aGP,
        "eGP": eGP,
        "iGP": iGP,
        "sfdps": sfdps,
        "sfps": sfps,
        "aps": aps,
        "eps": eps,
        "ips": ips,
        "adps": adps,
        "edps": edps,
        "idps": idps,
        "mdps": mdps,
        "stats": stats,
    }

    return data
