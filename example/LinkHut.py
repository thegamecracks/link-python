import link
import time

QUANTUM = 4  # beats per bar


def main() -> None:
    l = link.Link(120)
    l.enabled = True
    l.startStopSyncEnabled = True

    while True:
        s = l.captureSessionState()

        link_time = l.clock().micros()
        beats = s.beatAtTime(link_time, 0)
        phase = int(s.phaseAtTime(link_time, QUANTUM))
        phase = "X" * phase + "0" * (QUANTUM - phase)

        print(
            f"tempo {s.tempo():.2f} | "
            f"playing: {s.isPlaying()} | "
            f"beats {beats:.2f} | {phase}",
            end="\r",
            flush=True,
        )

        time.sleep(0.02)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
