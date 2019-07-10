# Timebox

Timebox is simple a command line script that you can use to create sets of reusable timers to play in order. In some ways it is similar to other 'pomodoro' timers with the added flexibility of creating your own set of timeboxed activities.

The idea came to me when I had a knee injury and needed to do sets of exercises multiple times a day. I would typically get distracted and lose my place in the set and lose count so found a time based audio approach to be better for me.

## Set up

You specify your timers in a yaml file. Where each timer can specify an interval or a list of intervals to go through. An interval timer can specify a duration, some text to say (only works on Mac) and a sound to play when the timer sequence starts. You can also specify a timer to be a list of timers which are then run through in order. For example you might want to be reminded to stand at your desk after sitting for a while so you could specify a `sit` timer with one duration and a `stand` timer with another and a `work` timer that is a `sit` followed by a `stand` etc.

You can then run the `work` timebox with the command

```
$ python timebox.py work
```

## Example YAML file

```
sit:
  duration: 20
  say: Sit and work
  play: Blow

stand:
  duration: 10
  say: stand and work
  play: Ping

break:
  duration: 10
  say: Take a break
  play: Ping

work:
  - sit
  - stand
  - sit
  - break

squats:
  say: Squats

leg_lifts:
  say: Leg lifts

clam_shell:
  say: clam shell

done:
  duration: 0
  say: Done

leg_set:
  - squats
  - leg_lifts
  - clam_shell
  - done

"10":
  - say: Ten minute timer
    duration: 10
  - say: Done
    play: Ping
    duration: 0

test:
  - say: start
    duration: .1
  - say: end
    duration: 0
```
