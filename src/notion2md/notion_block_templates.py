from mako.template import Template

paragraph_template = Template('${content}')

heading_1_template = Template('# ${content}')

heading_2_template = Template('## ${content}')

heading_3_template = Template('### ${content}')

# embed_template =  Template('### ${content}') # TODO: figure out how to get an embed block inside of revealJS