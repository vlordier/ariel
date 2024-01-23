"""
This module contains the models for the application.

The Flowchart class represents a flowchart and is a collection of nodes and links between them.
The Node class represents a node in a flowchart and has an identifier and a list of links to other nodes.
The Link class represents a link between two nodes in a flowchart and has a source and a target node and an optional label.
"""

from typing import List, Optional
from pydantic import BaseModel

class Node(BaseModel):
    """ 
    A class representing a node in a flowchart.
    Each node has an identifier and a list of links to other nodes.
    """
    identifier: str
    type: Optional[str] = None  # 'action' or 'condition'

class Link(BaseModel):
    """
    A class representing a link between two nodes in a flowchart.
    Each link has a source and a target node and an optional label.
    """
    source: str
    target: str
    label: Optional[str] = None

class Flowchart(BaseModel):
    """
    A class representing a flowchart.
    It is a collection of nodes and links between them.
    """
    nodes: List[Node]
    links: List[Link]


# class Node:
#     """
#     A class representing a node in a flowchart.
#     Each node has an identifier and a list of links to other nodes.
#     """

#     def __init__(self, identifier: str):
#         """Initialize the node with an identifier and an empty list of links."""
#         self.identifier = identifier
#         self.links: List[Link] = []

#     def add_link(self, link):
#         """Add a link to another node."""
#         self.links.append(link)

#     def __repr__(self):
#         """Return a string representation of the node."""
#         return f"Node({self.identifier})"


# class Link:
#     """
#     A class representing a link between two nodes in a flowchart.
#     Each link has a source and a target node and an optional label.
#     """

#     def __init__(self, source: Node, target: Node, label: Optional[str] = None):
#         self.source: Node = source
#         self.target: Node = target
#         self.label: Optional[str] = label

#     def __repr__(self):
#         """Return a string representation of the link."""
#         label_str = f" [{self.label}]" if self.label else ""
#         return f"{self.source.identifier} -->{label_str} {self.target.identifier}"


# class Flowchart:
#     """
#     A class representing a flowchart.
#     It is a collection of nodes and links between them.
#     """

#     def __init__(self) -> None:
#         """Initialize the Flowchart with an empty dictionary of nodes."""
#         self.nodes: Dict[str, Node] = {}

#     def add_node(self, node: Node) -> None:
#         """Add a node to the flowchart."""
#         if node.identifier not in self.nodes:
#             self.nodes[node.identifier] = node

#     def add_link(self, source: str, target: str, label: Optional[str] = None) -> None:
#         """Add a link between two nodes to the flowchart."""
#         source_node = self.nodes.get(source)
#         if not source_node:
#             source_node = Node(source)
#             self.add_node(source_node)
#         target_node = self.nodes.get(target)
#         if not target_node:
#             target_node = Node(target)
#             self.add_node(target_node)
#         link = Link(source_node, target_node, label)
#         source_node.add_link(link)

#     def remove_node(self, identifier: str) -> bool:
#         """Remove a node and its links from the flowchart."""
#         if identifier in self.nodes:
#             # Remove all links to and from this node
#             for node in self.nodes.values():
#                 node.links: List[Link] = [link for link in node.links if link.target.identifier != identifier]
#             del self.nodes[identifier]
#             return True
#         return False

#     def remove_link(self, source: str, target: str) -> bool:
#         """Remove a link between two nodes from the flowchart."""
#         source_node = self.nodes.get(source)
#         if source_node:
#             original_links_count: int = len(source_node.links)
#             source_node.links = [link for link in source_node.links if link.target.identifier != target]
#             return original_links_count != len(source_node.links)
#         return False

#     def update_link(self, source: str, target: str, new_label: Optional[str]) -> bool:
#         """Update the label of a link between two nodes in the flowchart."""
#         source_node = self.nodes.get(source)
#         if source_node:
#             for link in source_node.links:
#                 if link.target.identifier == target:
#                     link.label = new_label
#                     return True
#         return False

#     def get_node(self, identifier: str) -> Optional[Node]:
#         """Get a node from the flowchart."""
#         return self.nodes.get(identifier)
