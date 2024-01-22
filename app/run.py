"""
This is a simple flowchart executor that can execute a flowchart from a markdown file.
It is based on the Mermaid syntax for flowcharts.
"""

import logging
import os
from typing import List, Optional

class Node:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def __repr__(self):
        return f"Node({self.identifier})"

class Link:
    def __init__(self, source: Node, target: Node, label: Optional[str] = None):
        self.source = source
        self.target = target
        self.label = label

    def __repr__(self):
        label_str = f" [{self.label}]" if self.label else ""
        return f"{self.source.identifier} -->{label_str} {self.target.identifier}"

class Flowchart:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node: Node):
        self.nodes[node.identifier] = node

    def add_link(self, source: str, target: str, label: Optional[str] = None):
        source_node = self.nodes.get(source) or Node(source)
        target_node = self.nodes.get(target) or Node(target)
        link = Link(source_node, target_node, label)
        source_node.add_link(link)
        self.add_node(source_node)
        self.add_node(target_node)

    def get_node(self, identifier: str) -> Optional[Node]:
        return self.nodes.get(identifier)

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FlowchartExecutorV4:
    """A class for executing a flowchart from a markdown file."""

    def __init__(self, md_filepath: str):
        """
        Initialize the FlowchartExecutorV4 with a graph structure and prepare an empty log and Mermaid code.

        :param graph: A dictionary representing the flowchart graph where keys are node identifiers and
                      values are lists of tuples (edges) with target nodes and labels.
        """
        self.log: List[str] = []
        self.current_mermaid_code = self.parse_mermaid_from_markdown(
            markdown_file_path=md_filepath
        )
        if not self.current_mermaid_code:
            self.log.append(f"Mermaid code not found in markdown file: {md_filepath}")
            raise ValueError(f"Mermaid code not found in markdown file: {md_filepath}")
        self.flowchart = Flowchart()
        self.build_graph_from_mermaid_code(self.current_mermaid_code)

    def build_graph_from_mermaid_code(self, mermaid_code: str) -> None:
        """Build a graph from the Mermaid code."""
        graph = {}
        if mermaid_code:
            lines = mermaid_code.split("\n")
            for line in lines:
                line = line.strip()
                logger.info(f"Processing line: {line}")

                # Skip the first line of the Mermaid code block
                if (
                    line
                    and line.startswith("flowchart TD")
                    or line.startswith("graph TD")
                ):
                    continue

                if "-->" in line:
                    parts = line.split("-->")
                    from_node = parts[0].strip()
                    to_node_part = parts[1].strip()
                    to_node = ""
                    label = ""
                    # Check if there is a label
                    if "|" in to_node_part:
                        # Extract the label and the to_node
                        to_node, label = to_node_part.split("|", 1)
                        to_node = to_node.strip("[] ")
                        label = label.strip(" |")
                    else:
                        to_node = to_node_part.strip("[] ")
                    # Ensure that both from_node and to_node are valid before adding the link
                    if from_node and to_node:
                        if from_node not in graph:
                            graph[from_node] = []
                        graph[from_node].append((to_node, label))
                        self.flowchart.add_link(from_node, to_node, label)

    def parse_mermaid_from_markdown(self, markdown_file_path: str) -> Optional[str]:
        """Parse the Mermaid code from the markdown file."""
        if not os.path.exists(markdown_file_path):
            self.log.append(f"Markdown file not found: {markdown_file_path}")
            raise FileNotFoundError(f"Markdown file not found: {markdown_file_path}")

        if not markdown_file_path.endswith(".md"):
            self.log.append(
                f"Markdown file path must end with .md: {markdown_file_path}"
            )
            raise ValueError(
                f"Markdown file path must end with .md: {markdown_file_path}"
            )

        logger.info(f"Reading markdown file: {markdown_file_path}")

        mermaid_code = ""
        in_mermaid_block = False
        try:
            with open(markdown_file_path, encoding="utf-8") as md_file:
                for line in md_file:
                    if "```mermaid" in line:
                        in_mermaid_block = True
                    elif in_mermaid_block:
                        # Skip the line that starts the mermaid code block
                        if line.strip() == "```mermaid":
                            continue
                        # Check for the end of the mermaid code block
                        if line.strip() == "```":
                            in_mermaid_block = False
                            break
                        mermaid_code += line
            return mermaid_code
        except FileNotFoundError:
            self.log.append(f"Markdown file not found: {markdown_file_path}")
            return None

    def update_mermaid_code(self, current_node):
        # Updating the Mermaid code to reflect the current state of the flowchart
        self.current_mermaid_code = "flowchart TD\n"
        node = self.flowchart.get_node(current_node)
        if node:
            for edge in node.links:
                target = edge.target.identifier
                label = edge.label
                if label:
                    transition = f"{current_node} -->|{label}| {target}"
                else:
                    transition = f"{current_node} --> {target}"
                self.current_mermaid_code += f"    {transition}\n"
        self.log.append(f"Current Mermaid Code:\n{self.current_mermaid_code}")

    def execute_action(self, node, label):
        """
        Placeholder for actual action implementation.
        """
        action_desc = f"Executing action: {node}"
        if label:
            action_desc += f" with label: {label}"
        self.log.append(action_desc)

    def make_decision(self, decision_node, label) -> str:
        """
        Placeholder for actual decision implementation.
        Return the selected option.
        """
        decision_desc = f"Making decision at: {decision_node}"
        if label:
            decision_desc += f" with label: {label}"
        self.log.append(decision_desc)
        return self.graph[decision_node][0][0]  # Selecting the first option

    def run(self, start_node) -> None:
        """Run the flowchart starting from the given node."""
        current_node = start_node
        while True:
            self.update_mermaid_code(current_node)

            node = self.flowchart.get_node(current_node)
            if not node or not node.links:
                self.log.append(f"End of flow at: {current_node}")
                break

            next_step = node.links[0]  # Get the first transition
            next_node = next_step.target.identifier
            label = next_step.label

            if current_node.endswith("?}"):  # Decision node
                next_node = self.make_decision(current_node, label)
            else:
                self.execute_action(current_node, label)

            # Simulated reevaluation point
            self.log.append(
                "Reevaluation point: Prompt OpenAI GPT-4 for advice based on current state"
            )

            current_node = next_node

    def get_log(self) -> list:
        """
        Return the log of actions and decisions taken during the flowchart execution.
        """
        return self.log

    def get_current_mermaid_code(self) -> str:
        """
        Return the current Mermaid code representing the flowchart.
        """
        return self.current_mermaid_code


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Execute a flowchart from a markdown file."
    )
    parser.add_argument(
        "-m",
        "--markdown_file",
        help="The path to the markdown file containing the flowchart.",
        default="flows/skyscanner_ticket_booking.md",
    )
    args = parser.parse_args()

    markdown_file_path = args.markdown_file
    executor = FlowchartExecutorV4(md_filepath=markdown_file_path)
    executor.run("Start")

    for node_id, node in executor.flowchart.nodes.items():
        logger.info(f"Node {node_id}: Links - {node.links}")
