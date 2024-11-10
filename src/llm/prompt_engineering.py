from utils.logger import setup_logger

class PromptEngineering:
    """
    Utility class for crafting and managing prompts for LLMs.
    """

    def __init__(self, config):
        self.logger = setup_logger(config.get('logging', {}))
        self.prompt_templates = self._load_prompt_templates(config.get('templates_path', 'configs/prompts/'))
        self.logger.info("PromptEngineering initialized.")

    def _load_prompt_templates(self, templates_path):
        """
        Load prompt templates from the specified directory.

        Args:
            templates_path (str): Path to the prompt templates directory.

        Returns:
            dict: Dictionary of prompt templates.
        """
        import os
        import json
        self.logger.info(f"Loading prompt templates from {templates_path}")
        templates = {}
        for filename in os.listdir(templates_path):
            if filename.endswith('.json'):
                template_name = filename.replace('.json', '')
                with open(os.path.join(templates_path, filename), 'r') as file:
                    templates[template_name] = json.load(file)
                self.logger.debug(f"Loaded prompt template: {template_name}")
        return templates

    def get_prompt(self, template_name, **kwargs):
        """
        Retrieve and format a prompt template with provided parameters.

        Args:
            template_name (str): Name of the prompt template.
            **kwargs: Parameters to format the template.

        Returns:
            str: Formatted prompt.
        """
        self.logger.debug(f"Retrieving prompt for template: {template_name} with kwargs: {kwargs}")
        template = self.prompt_templates.get(template_name, "")
        if not template:
            self.logger.error(f"Prompt template '{template_name}' not found.")
            return ""
        try:
            prompt = template.format(**kwargs)
            self.logger.debug(f"Formatted prompt: {prompt}")
            return prompt
        except KeyError as e:
            self.logger.error(f"Missing parameter in prompt formatting: {e}")
            return ""