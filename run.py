"""
This is a simple flowchart executor that can execute a flowchart from a markdown file.
It is based on the Mermaid syntax for flowcharts.
"""

import logging
import os
from typing import List, Optional
from pydantic import BaseModel, ValidationError, parse_obj_as
from pydantic import TypeAdapter

from app.models import Flowchart, Node

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FlowchartExecutor:
    """A class for executing a flowchart from a markdown file."""

    def __init__(self, md_filepath: str) -> None:
        self.md_filepath = md_filepath
        self.log: List[str] = []
        self.flowchart = Flowchart(nodes=[], links=[])
        self.current_state: Optional[str] = None
        self.current_mermaid_code: str = ""
        self.parse_mermaid_from_markdown(md_file_path=self.md_filepath)
        self.build_graph_from_mermaid_code(self.current_mermaid_code)
    def build_graph_from_mermaid_code(self, mermaid_code: str) -> None:
        """Build a graph from the Mermaid code."""
        try:
            mermaid_flowchart_dict = self.parse_mermaid_code_to_dict(mermaid_code)
            mermaid_flowchart_dict = self.parse_mermaid_code_to_dict(mermaid_code)
            mermaid_flowchart = Flowchart.model_validate(mermaid_flowchart_dict)
            self.flowchart = mermaid_flowchart
            for node in mermaid_flowchart.nodes:
                self.flowchart.add_node(Node(node.identifier))
            for link in mermaid_flowchart.links:
                self.flowchart.add_link(link.source, link.target, link.label)
        except ValidationError as e:
            logger.error(f"Error validating Mermaid flowchart: {e}")
            raise


                    


    def parse_mermaid_code_to_dict(self, mermaid_code: str) -> dict:
        """
        Parse the Mermaid code string into a dictionary that can be used to create a MermaidFlowchart object.
        """
        nodes = []
        links = []
        lines = mermaid_code.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith('flowchart TD') or line.startswith('graph TD'):
                continue  # Skip the diagram type declaration
            if '-->' in line:
                # This is a link
                parts = line.split('-->')
                source = parts[0].strip()
                target_and_label = parts[1].split('|')
                target = target_and_label[0].strip()
                label = target_and_label[1].strip() if len(target_and_label) > 1 else None
                links.append({'source': source, 'target': target, 'label': label})
                if not any(node['identifier'] == source for node in nodes):
                    nodes.append({'identifier': source})
                if not any(node['identifier'] == target for node in nodes):
                    nodes.append({'identifier': target})
        return {'nodes': nodes, 'links': links}

    def parse_mermaid_from_markdown(self, md_file_path: str) -> Optional[str]:
        """Parse the Mermaid code from the markdown file."""
        if not os.path.exists(md_file_path):
            self.log.append(f"Markdown file not found: {md_file_path}")
            raise FileNotFoundError(f"Markdown file not found: {md_file_path}")

        if not md_file_path.endswith(".md"):
            self.log.append(f"Markdown file path must end with .md: {md_file_path}")
            raise ValueError(f"Markdown file path must end with .md: {md_file_path}")

        logger.info(f"Reading markdown file: {md_file_path}")

        mermaid_code = ""
        in_mermaid_block = False
        mermaid_data = {"nodes": [], "links": []}
        try:
            with open(md_file_path, encoding="utf-8") as md_file:
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
            return mermaid_code.lstrip()
            return mermaid_code.lstrip()
        except FileNotFoundError:
            self.log.append(f"Markdown file not found: {md_file_path}")
            return None

    def update_mermaid_code(self, current_node: Node) -> None:
        """

        Updating the Mermaid code to reflect the current state of the flowchart
        
        :param current_node: The current node identifier.
        """
        self.current_mermaid_code = self.dump_mermaid_code()
        self.log.append(f"Current Mermaid Code:\n{self.current_mermaid_code}")

    def dump_mermaid_code(self) -> str:
        """Generate the Mermaid code from the current state of the flowchart."""
        mermaid_code = "flowchart TD\n"
        

        mermaid_code += "flowchart TD\n"
        added_links = set()
      

        for node_id, node in self.flowchart.nodes.items():
            mermaid_code += f"    {node_id}\n"
            for link in node.links:
                link_str = f"    {link.source.identifier} -->"
                if link.label:
                    link_str += f"|{link.label}|"
                link_str += f" {link.target.identifier}\n"
                mermaid_code += link_str
        return mermaid_code.strip()

    def compare_with_original(self, original_code: str) -> None:
        """Compare the generated Mermaid code with the original code."""
        generated_code = self.dump_mermaid_code()
        if not generated_code:
            raise ValueError("Mermaid code is empty")
        if generated_code.strip() != original_code.strip():
            raise ValueError(
                "The generated Mermaid code does not match the original code.\n \
                Generated code:\n{generated_code}\n \
                Original code:\n{original_code}"
            )

    def execute_action(self, node: Node, label) -> None:
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

    def run(self, start_node: Optional[str] = None) -> None:
        """Run the flowchart starting from the given node or the first node if not provided."""
        self.current_state = start_node if start_node is not None else next(iter(self.flowchart.nodes), None)
        if not self.current_state:
            self.log.append("No start node found in the flowchart.")
            raise ValueError("No start node found in the flowchart.")
        current_node = self.current_state
        executed_nodes = set()
        while current_node:
            if current_node in executed_nodes:
                self.log.append(f"Loop detected at node: {current_node}, stopping execution.")
                break
            executed_nodes.add(current_node)

            node = self.flowchart.get_node(current_node)
            if not node:
                self.log.append(f"Node not found in flowchart: {current_node}")
                break

            if node.links:
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

                self.current_state = next_node
                current_node = self.current_state
            else:
                self.log.append(f"End of flow at: {current_node}")
                self.update_mermaid_code(current_node)
                break

            self.update_mermaid_code(current_node)

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
    executor = FlowchartExecutor(md_filepath=markdown_file_path)
    executor.run()  # Assuming "A" is the start node based on the provided Mermaid code
    logger.info("Execution log:")
    for log_entry in executor.get_log():
        logger.info(log_entry)

    # # Compare the generated Mermaid code with the original and raise an exception if they don't match
    # try:
    #     executor.compare_with_original(executor.current_mermaid_code)
    #     logger.info("The generated Mermaid code matches the original code.")
    # except ValueError as e:
    #     logger.error(str(e))
    #     raise

    for node_id, node in executor.flowchart.nodes.items():
        logger.info(f"Node {node_id}: Links - {node.links}")
