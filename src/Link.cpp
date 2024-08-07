#include <ableton/Link.hpp>
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>

PYBIND11_MODULE(_link, m, pybind11::mod_gil_not_used())
{
  using namespace ableton;
  using namespace pybind11;

  using Clock = Link::Clock;
  using SessionState = Link::SessionState;
  using micros = std::chrono::microseconds;

  class_<Clock>(m, "Clock")
      .def("micros", [](const Clock &clock)
           { return clock.micros().count(); });

  class_<SessionState>(m, "SessionState")
      .def("tempo", &SessionState::tempo)
      .def("setTempo", [](SessionState &sessionState, const double tempo, const uint64_t time)
           { sessionState.setTempo(tempo, micros(time)); })
      .def("beatAtTime", [](SessionState &sessionState, uint64_t time, double quantum)
           { return sessionState.beatAtTime(micros(time), quantum); })
      .def("phaseAtTime", [](SessionState &sessionState, uint64_t time, double quantum)
           { return sessionState.phaseAtTime(micros(time), quantum); })
      .def("timeAtBeat", [](SessionState &sessionState, double beat, double quantum)
           { return sessionState.timeAtBeat(beat, quantum).count(); })
      .def("requestBeatAtTime", [](SessionState &sessionState, double beat, uint64_t time, double quantum)
           { sessionState.requestBeatAtTime(beat, micros(time), quantum); })
      .def("isPlaying", &SessionState::isPlaying)
      .def("setIsPlaying", [](SessionState &sessionState, const bool isPlaying, const uint64_t time)
           { sessionState.setIsPlaying(isPlaying, micros(time)); })
      .def("forceBeatAtTime", [](SessionState &sessionState, double beat, uint64_t time, double quantum)
           { sessionState.forceBeatAtTime(beat, micros(time), quantum); })
      .def("timeForIsPlaying", [](SessionState &sessionState)
           { return sessionState.timeForIsPlaying().count(); })
      .def("requestBeatAtStartPlayingTime", [](SessionState &sessionState, double beat, double quantum)
           { sessionState.requestBeatAtStartPlayingTime(beat, quantum); })
      .def("setIsPlayingAndRequestBeatAtTime", [](SessionState &sessionState, bool isPlaying, uint64_t time, double beat, double quantum)
           { sessionState.setIsPlayingAndRequestBeatAtTime(isPlaying, micros(time), beat, quantum); })
  ;

  class_<Link>(m, "Link")
      .def(init<const double &>())
      .def_property("enabled", &Link::isEnabled, &Link::enable)
      .def("numPeers", &Link::numPeers)
      .def("clock", &Link::clock)

      .def("captureAppSessionState", &Link::captureAppSessionState)
      .def("commitAppSessionState", &Link::commitAppSessionState)
      // Aliases for backwards-compatibility
      .def("captureSessionState", &Link::captureAppSessionState)
      .def("commitSessionState", &Link::commitAppSessionState)

      .def_property("startStopSyncEnabled",
                    &Link::isStartStopSyncEnabled, &Link::enableStartStopSync)
      .def("setNumPeersCallback", [](Link &link, const std::function<void(std::size_t)> &callback)
           { link.setNumPeersCallback(callback); })
      .def("setTempoCallback", [](Link &link, const std::function<void(double)> &callback)
           { link.setTempoCallback(callback); })
      .def("setStartStopCallback", [](Link &link, const std::function<void(bool)> &callback)
           { link.setStartStopCallback(callback); })
  ;
}
