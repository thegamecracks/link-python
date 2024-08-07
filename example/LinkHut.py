import link
import time

QUANTUM = 4  # beats per bar


def main() -> None:
    l = link.Link(120)
    l.enabled = True
    l.startStopSyncEnabled = True

    print("enabled | num peers | quantum | start stop sync | tempo   | beats   | metro")

    while True:
        s = l.captureSessionState()

        link_time = l.clock().micros()
        enabled = "yes" if l.enabled else "no"
        peers = l.numPeers()
        start_stop_sync = "yes" if l.startStopSyncEnabled else "no"
        playing = "[playing]" if s.isPlaying() else "[stopped]"
        beats = s.beatAtTime(link_time, 0)
        phase = int(s.phaseAtTime(link_time, QUANTUM)) + 1
        metro = "X" * phase + "0" * (QUANTUM - phase)

        print(
            f"{enabled:<7s} | "
            f"{peers:<9d} | "
            f"{QUANTUM:<7d} | "
            f"{start_stop_sync:<3s} {playing:<11s} | "
            f"{s.tempo():<7.2f} | "
            f"{beats:<7.2f} | "
            f"{metro}",
            end="\r",
            flush=True,
        )

        time.sleep(0.02)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
