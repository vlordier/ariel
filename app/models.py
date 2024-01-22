"""
This module contains the models for the application.

The Flowchart class represents a flowchart and is a collection of nodes and links between them.
The Node class represents a node in a flowchart and has an identifier and a list of links to other nodes.
The Link class represents a link between two nodes in a flowchart and has a source and a target node and an optional label.
"""

from typing import List, Optional


class Node:
    """
    A class representing a node in a flowchart.
    Each node has an identifier and a list of links to other nodes.
    """

    def __init__(self, identifier: str):
        """Initialize the node with an identifier and an empty list of links."""
        self.identifier = identifier
        self.links: List[Link] = []

    def add_link(self, link):
        """Add a link to another node."""
        self.links.append(link)

    def __repr__(self):
        """Return a string representation of the node."""
        return f"Node({self.identifier})"


class Link:
    """
    A class representing a link between two nodes in a flowchart.
    Each link has a source and a target node and an optional label.
    """

    def __init__(self, source: Node, target: Node, label: Optional[str] = None):
        self.source = source
        self.target = target
        self.label = label

    def __repr__(self):
        """Return a string representation of the link."""
        label_str = f" [{self.label}]" if self.label else ""
        return f"{self.source.identifier} -->{label_str} {self.target.identifier}"


class Flowchart:
    """
    A class representing a flowchart.
    It is a collection of nodes and links between them.
    """

    def __init__(self) -> None:
        """Initialize the Flowchart with an empty dictionary of nodes."""
        self.nodes = {}

    def add_node(self, node: Node) -> None:
        """Add a node to the flowchart."""
        self.nodes[node.identifier] = node

    def add_link(self, source: str, target: str, label: Optional[str] = None) -> None:
        """Add a link between two nodes to the flowchart."""
        source_node = self.nodes.get(source) or Node(source)
        target_node = self.nodes.get(target) or Node(target)
        link = Link(source_node, target_node, label)
        source_node.add_link(link)
        self.add_node(source_node)
        self.add_node(target_node)

    def get_node(self, identifier: str) -> Optional[Node]:
        """Get a node from the flowchart."""
        return self.nodes.get(identifier)
