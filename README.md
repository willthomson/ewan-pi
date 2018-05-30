# ewan-pi

Ewan the Dream Sheep controlled by Raspberry Pi relay board.

![Photo of a Raspberry Pi with a relay board and the internals of a Ewan](https://raw.githubusercontent.com/willthomson/ewan-pi/master/ewan-pi.jpg)

When my son was stirs, the sounds from Ewan help him go back to sleep.
However, going into the room to start it wakes him up. I wanted a way
to start Ewan without entering the room, so I created a simple Flask app,
running on a Raspberry Pi, which uses a relay board to simulate pressing
the buttons.

## Hardware

* Rapsberry Pi 2
* USB wifi adapter
* Relay board
* Electronics from a Ewan, sourced second hand from Ebay

I attached the relay board to the Raspberry Pi, then cut the button off of
the desired sound and connected it to one of the relays.

# Development

1. `pip install -r requirements.txt`
1. `FLASK_APP=app.py flask run`
