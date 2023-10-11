
from __future__ import annotations

import re
import json
from typing import Union

from agentverse.parser import OutputParser, LLMResult
from agentverse.utils import AgentAction, AgentFinish
from agentverse.parser import OutputParserError, output_parser_registry

# Athlete Parser
@output_parser_registry.register("athlete")
class AthleteParser(OutputParser):
    def parse(self, output: LLMResult) -> Union[AgentAction, AgentFinish]:
        text = output.text
        try:
            thought = re.search(r'Thought: (.+)', text).group(1)
            action = re.search(r'Action: (.+)', text).group(1)
            return AgentAction({'thought': thought, 'action': action})
        except AttributeError:
            raise OutputParserError("Unable to parse Athlete output.")

# Trainer Parser
@output_parser_registry.register("trainer")
class TrainerParser(OutputParser):
    def parse(self, output: LLMResult) -> Union[AgentAction, AgentFinish]:
        text = output.text
        try:
            strategy = re.search(r'Strategy: (.+)', text).group(1)
            action = re.search(r'Action: (.+)', text).group(1)
            return AgentAction({'strategy': strategy, 'action': action})
        except AttributeError:
            raise OutputParserError("Unable to parse Trainer output.")

# Arena Owner Parser
@output_parser_registry.register("arena_owner")
class ArenaOwnerParser(OutputParser):
    def parse(self, output: LLMResult) -> Union[AgentAction, AgentFinish]:
        text = output.text
        try:
            decision = re.search(r'Decision: (.+)', text).group(1)
            action = re.search(r'Action: (.+)', text).group(1)
            return AgentAction({'decision': decision, 'action': action})
        except AttributeError:
            raise OutputParserError("Unable to parse Arena Owner output.")
