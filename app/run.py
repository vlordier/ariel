class FlowchartExecutorV4:
    def __init__(self, graph):
        self.graph = graph
        self.log = []
        self.current_mermaid_code = ""

    def parse_mermaid_from_markdown(self, markdown_file_path):
        mermaid_code = ""
        in_mermaid_block = False
        try:
            with open(markdown_file_path) as md_file:
                for line in md_file:
                    if line.strip() == "```mermaid":
                        in_mermaid_block = True
                    elif line.strip() == "```" and in_mermaid_block:
                        in_mermaid_block = False
                        break
                    elif in_mermaid_block:
                        mermaid_code += line
            return mermaid_code
        except FileNotFoundError:
            self.log.append(f"Markdown file not found: {markdown_file_path}")
            return None

    def update_mermaid_code(self, current_node):
        # Updating the Mermaid code to reflect the current state of the flowchart
        self.current_mermaid_code = "flowchart TD\n"
        for node, edges in self.graph.items():
            for edge in edges:
                target, label = edge
                if label:
                    transition = f"{node} -->|{label}| {target}"
                else:
                    transition = f"{node} --> {target}"
                self.current_mermaid_code += f"    {transition}\n"
        self.log.append(f"Current Mermaid Code:\n{self.current_mermaid_code}")

    def execute_action(self, node, label):
        # Placeholder for actual action implementation
        action_desc = f"Executing action: {node}"
        if label:
            action_desc += f" with label: {label}"
        self.log.append(action_desc)

    def make_decision(self, decision_node, label) -> str:
        # Placeholder for decision-making logic
        decision_desc = f"Making decision at: {decision_node}"
        if label:
            decision_desc += f" with label: {label}"
        self.log.append(decision_desc)
        return self.graph[decision_node][0][0]  # Selecting the first option

    def run(self, start_node) -> None:
        current_node = start_node
        while True:
            self.update_mermaid_code(current_node)

            if current_node not in self.graph or not self.graph[current_node]:
                self.log.append(f"End of flow at: {current_node}")
                break

            next_step = self.graph[current_node][0]  # Get the first transition
            next_node, label = next_step

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
        return self.log

    def get_current_mermaid_code(self) -> str:
        return self.current_mermaid_code
