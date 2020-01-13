#!/usr/bin/env python3
from tictactoe import app
from tictactoe.datatbase import init_db

if __name__ == "__main__":
    init_db()
    app.run(debug=True, threaded=True)