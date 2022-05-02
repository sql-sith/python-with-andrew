import re

'''a limited parser to converted markdown to html.

this parser converts the following markdown elements to html:

    this becomes this                   comments
--------         ---------------------- -------------------------------------------
       #         <h1>
      ##         <h2>
     ###         <h3>
    ####         <h4>
   #####         <h5>
  ######         <h6>
       -         <li>                   the <ul> container element is introduced 
                                        when needed and closed when it should be.
       1.        <li>                   the <ol> container element is introduced
                                        when needed and closed when it should be.
 __text__        <strong>text</strong>
   _text_        <em>text</em>
plaintext        <p>plaintext</p>
'''


class ConvertedDocument:

    def __init__(self, source_document):
        """Converts a source document, which is assumed to be in a simplified Markdown format, to html.

        :param source_document: string: the input Markdown document
        """
        self.source_document = source_document
        self.converted_document = ''

        markdown_lines = self.source_document.split('\n')

        current_list_state = None

        for markdown_line in markdown_lines:
            html_line, new_list_state = self.apply_parsing_rules(markdown_line)

            # html_line, current_list_state = self.handle_list_state(html_line, current_list_state, new_list_state)

            if (current_list_state and new_list_state) and (current_list_state != new_list_state):
                raise ValueError(
                    f"Detected list item(s) of type <{new_list_state}> " +
                    f"but the current list is of type <{current_list_state}>."
                )
            elif (not current_list_state) and new_list_state:
                html_line = f"<{new_list_state}>{html_line}"
                current_list_state = new_list_state
            elif current_list_state and (not new_list_state):
                html_line = f"</{current_list_state}>{html_line}"
                current_list_state = None

            self.converted_document += html_line

        if current_list_state:
            self.converted_document += f"</{current_list_state}>"

    def apply_parsing_rules(self, markdown_line):
        """Applies self.parsing_rules() to the markdown_line argument.

        :param markdown_line: string:         This is a string assumed to be in Markdown format.
                                              This method will convert it to HTML.
        :return: html_line: html_line is the HTML version of markdown_line.
                                              active_list_type lets the caller know if a list is currently
                                              active, and if so, what type of list it is. The values for
                                              this attribute are defined in self.parsing_rules().
                 active_list_type:
        """

        html_line = markdown_line
        active_list_type = None

        for rule in self.parsing_rules(self):
            # print(rule["name"])
            search_pattern = rule["search_pattern"]
            replace_type = rule["replace_type"]

            if replace_type == "function":
                m = re.match(search_pattern, html_line)
                if m:
                    replace_function = rule["replace_function"]
                    html_line = replace_function(m.groups())
            elif replace_type == "sub":
                # list rules have replace_type == "sub" so we will handle list types here:
                candidate_list_type = None
                try:
                    candidate_list_type = rule["list_type"]
                except KeyError:
                    pass

                replace_pattern = rule["replace_pattern"]
                html_line, subs = re.subn(search_pattern, replace_pattern, html_line)
                if subs > 0 and candidate_list_type:
                    active_list_type = candidate_list_type

        return html_line, active_list_type

    @staticmethod
    def change_markdown_header_to_html(split_header_line):
        """Replaces a Markdown header with the corresponding HTML header.

        This function converts a Markdown line that starts with one to six dashes to an HTML line
        with the appropriate header tag from <H1> through <H6>, depending on the number of hashtags
        found in the Markdown line.


        :param split_header_line: list - a list containing two items:
                                            1) the Markdown hashtag prefix; and
                                            2) the rest of the line.
        """
        hashtags = split_header_line[0]
        rest_of_line = split_header_line[1]
        header_level = len(hashtags)
        return f'<h{header_level}>{rest_of_line}</h{header_level}>'

    @staticmethod
    def parsing_rules(self):
        # array of parsing patterns (each is a regex).
        # the name attribute just makes the rules easy to identify when debugging.
        return [
            {
                "name": "header",
                "search_pattern": r'^(#{1,6}) (.*)$',
                "replace_type": "function",
                "replace_function": self.change_markdown_header_to_html,
                "note": "if re.match() is successful, pass in re.groups() to change_markdown_to_html()."
            },
            {
                "name": "unordered list item",
                "list_type": "ul",
                "search_pattern": r'^[-\*] (.*)',
                "replace_type": "sub",
                "replace_pattern": r'<li>\g<1></li>'
            },
            {
                "name": "ordered list item",
                "list_type": "ol",
                "search_pattern": r'^(\d+)\. (.*)',
                "replace_type": "sub",
                "replace_pattern": r'<li>\g<1></li>'
            },
            {
                "name": "strong/bold",
                "search_pattern": r'(.*)__(.*)__(.*)',
                "replace_type": "sub",
                "replace_pattern": r'\g<1><strong>\g<2></strong>\g<3>'
            },
            {
                "name": "emphasis/italic",
                "search_pattern": r'(.*)_(.*)_(.*)',
                "replace_type": "sub",
                "replace_pattern": r'\g<1><em>\g<2></em>\g<3>'
            },
            {
                "name": "paragraph",
                "search_pattern": '^(?!(?:<h[1-6]>|</?ul>|</?ol>|</?li>))(.*)$',
                "replace_type": "sub",
                "replace_pattern": r'<p>\g<1></p>'
            }
        ]


def parse(markdown_document):
    return ConvertedDocument(markdown_document).converted_document
