# Docstrings derived from:
# https://github.com/Ableton/link/blob/Link-3.0.6/include/ableton/Link.hpp

from typing import Any, Callable

class Clock:
    def micros(self) -> int:
        """Return the current system time in microseconds."""

class SessionState:
    def tempo(self) -> float:
        """Return the tempo of the timeline, in Beats Per Minute.

        This is a stable value that is appropriate for display
        to the user. Beat time progress will not necessarily match this tempo
        exactly because of clock drift compensation.

        """

    def setTempo(self, __tempo: float, __time: int) -> None:
        """Set the timeline tempo to the given bpm value, taking
        effect at the given time.
        """

    def beatAtTime(self, __time: int, __quantum: float) -> float:
        """Get the beat value corresponding to the given time
        for the given quantum.

        The magnitude of the resulting beat value is
        unique to this Link instance, but its phase with respect to
        the provided quantum is shared among all session
        peers. For non-negative beat values, the following
        property holds: fmod(beatAtTime(t, q), q) == phaseAtTime(t, q)

        """

    def phaseAtTime(self, __time: int, __quantum: float) -> float:
        """Get the session phase at the given time for the given
        quantum.

        The result is in the interval [0, quantum). The
        result is equivalent to fmod(beatAtTime(t, q), q) for
        non-negative beat values. This method is convenient if the
        client is only interested in the phase and not the beat
        magnitude. Also, unlike fmod, it handles negative beat values
        correctly.

        """

    def timeAtBeat(self, __beat: float, __quantum: float) -> float:
        """Get the time at which the given beat occurs for the
        given quantum.

        The inverse of beatAtTime, assuming a constant
        tempo. beatAtTime(timeAtBeat(b, q), q) === b.

        """

    def requestBeatAtTime(self, __beat: float, __time: int, __quantum: float) -> None:
        """Attempt to map the given beat to the given time in the
        context of the given quantum.

        This method behaves differently depending on the
        state of the session. If no other peers are connected,
        then this instance is in a session by itself and is free to
        re-map the beat/time relationship whenever it pleases. In this
        case, beatAtTime(time, quantum) == beat after this method has
        been called.

        If there are other peers in the session, this instance
        should not abruptly re-map the beat/time relationship in the
        session because that would lead to beat discontinuities among
        the other peers. In this case, the given beat will be mapped
        to the next time value greater than the given time with the
        same phase as the given beat.

        This method is specifically designed to enable the concept of
        "quantized launch" in client applications. If there are no other
        peers in the session, then an event (such as starting
        transport) happens immediately when it is requested. If there
        are other peers, however, we wait until the next time at which
        the session phase matches the phase of the event, thereby
        executing the event in-phase with the other peers in the
        session. The client only needs to invoke this method to
        achieve this behavior and should not need to explicitly check
        the number of peers.

        """

    def isPlaying(self) -> bool:
        """Return True if the transport is playing, False otherwise."""

    def setIsPlaying(self, __isPlaying: bool, __time: int) -> None:
        """Set if transport should be playing or stopped, taking effect
        at the given time.
        """

    def forceBeatAtTime(self, __beat: float, __time: int, __quantum: float) -> None:
        """Rudely re-map the beat/time relationship for all peers
        in a session.

        DANGER: This method should only be needed in
        certain special circumstances. Most applications should not
        use it. It is very similar to requestBeatAtTime except that it
        does not fall back to the quantizing behavior when it is in a
        session with other peers. Calling this method will
        unconditionally map the given beat to the given time and
        broadcast the result to the session. This is very anti-social
        behavior and should be avoided.

        One of the few legitimate uses of this method is to
        synchronize a Link session with an external clock source. By
        periodically forcing the beat/time mapping according to an
        external clock source, a peer can effectively bridge that
        clock into a Link session. Much care must be taken at the
        application layer when implementing such a feature so that
        users do not accidentally disrupt Link sessions that they may
        join.

        """

    def timeForIsPlaying(self) -> int:
        """Get the time in microseconds at which a transport start/stop occurs."""

    def requestBeatAtStartPlayingTime(self, __beat: float, __quantum: float) -> None:
        """Convenience function to attempt to map the given beat to the time
        when transport is starting to play in context of the given quantum.

        This function evaluates to a no-op if isPlaying() equals false.

        """

    def setIsPlayingAndRequestBeatAtTime(
        self,
        __isPlaying: bool,
        __time: int,
        __beat: float,
        __quantum: float,
    ) -> None:
        """Convenience function to start or stop transport at a given time and
        attempt to map the given beat to this time in context of the given quantum.
        """

class Link:
    """Represents a participant in a Link session.

    Each Link instance has its own session state which
    represents a beat timeline and a transport start/stop state. The
    timeline starts running from beat 0 at the initial tempo when
    constructed. The timeline always advances at a speed defined by
    its current tempo, even if transport is stopped. Synchronizing to the
    transport start/stop state of Link is optional for every peer.
    The transport start/stop state is only shared with other peers when
    start/stop synchronization is enabled.

    A Link instance is initially disabled after construction, which
    means that it will not communicate on the network. Once enabled,
    a Link instance initiates network communication in an effort to
    discover other peers. When peers are discovered, they immediately
    become part of a shared Link session.

    """

    enabled: bool
    """Indicates if Link is currently enabled.

    To start Link, set this attribute to True.

    """

    startStopSyncEnabled: bool
    """Indicates if start/stop synchronization is enabled.

    To enable start/stop synchronization, set this attribute to True.

    """

    def __init__(self, __bpm: float) -> None:
        """
        :param bpm: The initial tempo of the session.
        """

    def numPeers(self) -> int:
        """Return the number of peers currently connected in the Link session."""

    def clock(self) -> Clock:
        """Return the clock used by Link.

        The Clock type is a platform-dependent representation
        of the system clock. It exposes a micros() method, which is a
        normalized representation of the current system time in
        microseconds.

        """

    def captureAppSessionState(self) -> SessionState:
        """Capture the current Link Session State from an application thread.

        Provides a mechanism for capturing the Link Session
        State from an application thread (other than the audio thread).
        The returned Session State stores a snapshot of the current Link
        state, so it should be captured and used in a local scope.
        Storing the it for later use in a different context is not
        advised because it will provide an outdated view.

        """

    def commitAppSessionState(self, __state: SessionState) -> None:
        """Commit the given Session State to the Link session from an
        application thread.

        The given Session State will replace the current Link
        Session State. Modifications of the Session State will be
        communicated to other peers in the session.

        :param state: The session state to be committed.

        """

    captureSessionState = captureAppSessionState
    commitSessionState = commitAppSessionState

    def setNumPeersCallback(self, __callback: Callable[[int], Any]) -> None:
        """Register a callback to be notified when the number of
        peers in the Link session changes.

        The callback is invoked on a Link-managed thread.

        :param callback:
            The callback to be invoked. It should take one argument,
            the new number of peers.

        """

    def setTempoCallback(self, __callback: Callable[[float], Any]) -> None:
        """Register a callback to be notified when the session
        tempo changes.

        The callback is invoked on a Link-managed thread.

        :param callback:
            The callback to be invoked. It should take one argument,
            the new tempo.

        """

    def setStartStopCallback(self, __callback: Callable[[bool], Any]) -> None:
        """Register a callback to be notified when the state of
        start/stop isPlaying changes.

        The callback is invoked on a Link-managed thread.

        :param callback:
            The callback to be invoked. It should take one argument,
            the new start/stop state.

        """
