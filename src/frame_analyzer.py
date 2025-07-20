import re
from dataclasses import dataclass

@dataclass
class FrameEvent:
    timestamp: str
    object: str
    location: str
    action: str

def parse_description(frame_desc):
    """
    Converts free-text like 'Blue truck spotted at Gate'
    into FrameEvent(object='Blue truck', location='Gate', action='spotted')
    """
    pattern = r"(.+?) (spotted|seen|observed) at (.+)"
    match = re.match(pattern, frame_desc.description)
    
    if match:
        obj, action, loc = match.groups()
        return FrameEvent(
            timestamp=frame_desc.timestamp,
            object=obj.strip(),
            location=loc.strip(),
            action=action.strip()
        )
    else:
        # fallback: return None or basic fallback
        return FrameEvent(
            timestamp=frame_desc.timestamp,
            object="Unknown",
            location="Unknown",
            action="Unrecognized"
        )

if __name__ == "__main__":
    from input_generator import generate_sample_data

    _, frames = generate_sample_data()

    print("\n--- Parsed Frame Events ---")
    for frame in frames:
        event = parse_description(frame)
        print(event)
