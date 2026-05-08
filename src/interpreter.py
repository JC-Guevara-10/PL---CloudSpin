KEYWORD_MEANINGS = {
    "SPIN UP":    "New server instance successfully created and initialized.",
    "SCALE":      "Adjusting instance count to meet demand requirements.",
    "WAIT UNTIL": "System paused. Awaiting specified condition...",
    "SPIN DOWN":  "Individual server instance stopped.",
    "PARSE":      "Analyzing input commands; building execution tree.",
    "EXECUTE":    "Running deployment tasks. Concurrent operations started.",
    "LOG":        "Activity recorded. Syncing logs to primary console.",
    "TERMINATE":  "Simulation ended. All resources released.",
}

def interpreter(keyword: str) -> str:
    """
    INTERPRETER — Executes the meaning of the keyword.

    Looks up the keyword in the meaning table and returns its description.
    """
    return KEYWORD_MEANINGS.get(keyword, "Unknown keyword.")