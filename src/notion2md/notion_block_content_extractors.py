from notional.blocks import Heading1

def heading_1_content_extractor(heading1:Heading1)->str:
    return ' '.join(text.text.content for text in heading1.heading_1.text)