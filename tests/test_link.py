from link import Link


def test_for_smoke() -> None:
    tempo = 120
    link = Link(tempo)

    clock = link.clock()
    micros = clock.micros()

    state = link.captureAppSessionState()
    assert state.tempo() == tempo
    beat = state.beatAtTime(micros, 4)
    assert state.timeAtBeat(beat, 4) == micros
    state.phaseAtTime(micros, 4)
    state.isPlaying()
    state.timeForIsPlaying()

    link.numPeers()
    link.setNumPeersCallback(lambda num_peers: 1)
    link.setTempoCallback(lambda tempo: 1)
    link.setStartStopCallback(lambda playing: 1)
