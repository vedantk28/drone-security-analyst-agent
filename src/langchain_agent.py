import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.agents import initialize_agent, AgentType
from langchain_huggingface import HuggingFaceEndpoint
from src.langchain_tools import (
    QueryDetectionsTool,
    AlertCheckTool,
    RetrieverTool,
    FrameRetrieverTool
)

# 🛠️ Define agent tools
tools = [
    QueryDetectionsTool,
    AlertCheckTool,
    RetrieverTool,
    FrameRetrieverTool
]

# 🔍 Debug tool information
def debug_tools():
    """Debug tool information to understand their structure"""
    print("🔧 DEBUGGING TOOL INFORMATION")
    print("="*50)
    
    tool_instances = [QueryDetectionsTool, AlertCheckTool, RetrieverTool, FrameRetrieverTool]
    
    for tool in tool_instances:
        try:
            # Check if it's already an instance or needs to be instantiated
            if hasattr(tool, 'name'):
                # It's already a tool instance
                tool_instance = tool
                print(f"\n📋 {tool.name}:")
            else:
                # It's a class, need to instantiate
                tool_instance = tool()
                print(f"\n📋 {tool.__name__}:")
            
            print(f"  - Type: {type(tool_instance)}")
            print(f"  - Available methods: {[method for method in dir(tool_instance) if not method.startswith('_')]}")
            
            # Check if it has the expected methods
            if hasattr(tool_instance, 'invoke'):
                print(f"  - ✅ Has invoke() method")
            if hasattr(tool_instance, 'run'):
                print(f"  - ✅ Has run() method")
            if hasattr(tool_instance, '_run'):
                print(f"  - ✅ Has _run() method")
                
            # Try to get tool description
            if hasattr(tool_instance, 'description'):
                print(f"  - Description: {tool_instance.description}")
            if hasattr(tool_instance, 'name'):
                print(f"  - Name: {tool_instance.name}")
                
        except Exception as e:
            print(f"  - ❌ Error with tool: {e}")

# 🌐 Solution 1: Manual tool execution (most reliable)
def execute_manual_workflow():
    """Execute tools manually without agent complexity"""
    
    query = "Investigate any suspicious events involving buses or crowds near the Garage"
    print(f"🔍 Investigation Query: {query}")
    print("="*60)
    
    # First debug the tools
    debug_tools()
    print("\n" + "="*60)
    print("🚀 STARTING INVESTIGATION")
    print("="*60)
    
    results = {}
    
    # Step 1: Check alerts
    print("\n📋 Step 1: Checking for triggered alerts...")
    try:
        # AlertCheckTool is already an instance, not a class
        alert_tool = AlertCheckTool
        alert_result = alert_tool.invoke("")
        results['alerts'] = alert_result
        print(f"✅ Alert Result: {alert_result}")
    except Exception as e:
        print(f"❌ Alert check failed: {e}")
        # Try alternative calling methods
        try:
            alert_result = alert_tool.run("")
            results['alerts'] = alert_result
            print(f"✅ Alert Result (via run): {alert_result}")
        except Exception as e2:
            try:
                alert_result = alert_tool._run("")
                results['alerts'] = alert_result
                print(f"✅ Alert Result (via _run): {alert_result}")
            except Exception as e3:
                print(f"❌ Alert check failed all methods: invoke={e}, run={e2}, _run={e3}")
                results['alerts'] = f"Error: {e}"
    
    # Step 2: Query detections for buses
    print("\n🚌 Step 2: Searching for bus detections...")
    try:
        query_tool = QueryDetectionsTool
        bus_result = query_tool.invoke("bus")
        results['bus_detections'] = bus_result
        print(f"✅ Bus detections: {bus_result}")
    except Exception as e:
        print(f"❌ Bus query failed: {e}")
        try:
            bus_result = query_tool.run("bus")
            results['bus_detections'] = bus_result
            print(f"✅ Bus detections (via run): {bus_result}")
        except Exception as e2:
            try:
                bus_result = query_tool._run("bus")
                results['bus_detections'] = bus_result
                print(f"✅ Bus detections (via _run): {bus_result}")
            except Exception as e3:
                print(f"❌ Bus query failed all methods: {e}")
                results['bus_detections'] = f"Error: {e}"
    
    # Step 3: Query detections for crowds/people
    print("\n👥 Step 3: Searching for people/crowd detections...")
    try:
        query_tool = QueryDetectionsTool  # Same tool instance
        people_result = query_tool.invoke("person")
        results['people_detections'] = people_result
        print(f"✅ People detections: {people_result}")
    except Exception as e:
        print(f"❌ People query failed: {e}")
        try:
            people_result = query_tool.run("person")
            results['people_detections'] = people_result
            print(f"✅ People detections (via run): {people_result}")
        except Exception as e2:
            try:
                people_result = query_tool._run("person")
                results['people_detections'] = people_result
                print(f"✅ People detections (via _run): {people_result}")
            except Exception as e3:
                print(f"❌ People query failed all methods: {e}")
                results['people_detections'] = f"Error: {e}"
    
    # Step 4: Semantic search near garage
    print("\n🏢 Step 4: Searching for events near garage...")
    try:
        retriever_tool = RetrieverTool
        garage_result = retriever_tool.invoke("suspicious activity near garage")
        results['garage_events'] = garage_result
        print(f"✅ Garage area events: {garage_result}")
    except Exception as e:
        print(f"❌ Garage search failed: {e}")
        try:
            garage_result = retriever_tool.run("suspicious activity near garage")
            results['garage_events'] = garage_result
            print(f"✅ Garage area events (via run): {garage_result}")
        except Exception as e2:
            try:
                garage_result = retriever_tool._run("suspicious activity near garage")
                results['garage_events'] = garage_result
                print(f"✅ Garage area events (via _run): {garage_result}")
            except Exception as e3:
                print(f"❌ Garage search failed all methods: {e}")
                results['garage_events'] = f"Error: {e}"
    
    # Step 5: Frame retrieval for visual context
    print("\n🖼️ Step 5: Retrieving visual frames...")
    try:
        frame_tool = FrameRetrieverTool
        frame_result = frame_tool.invoke("bus crowd garage")
        results['visual_frames'] = frame_result
        print(f"✅ Visual frames: {frame_result}")
    except Exception as e:
        print(f"❌ Frame retrieval failed: {e}")
        try:
            frame_result = frame_tool.run("bus crowd garage")
            results['visual_frames'] = frame_result
            print(f"✅ Visual frames (via run): {frame_result}")
        except Exception as e2:
            try:
                frame_result = frame_tool._run("bus crowd garage")
                results['visual_frames'] = frame_result
                print(f"✅ Visual frames (via _run): {frame_result}")
            except Exception as e3:
                print(f"❌ Frame retrieval failed all methods: {e}")
                results['visual_frames'] = f"Error: {e}"
    
    # Summary
    print("\n" + "="*60)
    print("🧠 INVESTIGATION SUMMARY")
    print("="*60)
    
    for step, result in results.items():
        print(f"\n{step.upper().replace('_', ' ')}: {result}")
    
    return results

# 🌐 Solution 2: Simplified agent with basic error handling
def create_simple_agent():
    """Create a simple agent with minimal complexity"""
    
    try:
        # Use a reliable model
        llm = HuggingFaceEndpoint(
            repo_id="microsoft/DialoGPT-medium",
            task="text-generation",
            huggingfacehub_api_token="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",
            max_new_tokens=256,
            temperature=0.1,
            repetition_penalty=1.1
        )
        
        # Create simple agent
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3,
            early_stopping_method="generate"
        )
        
        return agent
        
    except Exception as e:
        print(f"❌ Agent creation failed: {e}")
        return None

# 🌐 Solution 3: Alternative model approach  
def create_alternative_agent():
    """Try with a different model that might work better"""
    
    try:
        # Try Flan-T5 which is good for following instructions
        llm = HuggingFaceEndpoint(
            repo_id="google/flan-t5-small",
            task="text2text-generation",
            huggingfacehub_api_token="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",
            max_new_tokens=200,
            temperature=0.1
        )
        
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=2
        )
        
        return agent
        
    except Exception as e:
        print(f"❌ Alternative agent creation failed: {e}")
        return None

# 🌐 Solution 4: Local transformers pipeline
def create_local_agent():
    """Create agent using local transformers pipeline"""
    
    try:
        from transformers import pipeline
        from langchain_community.llms import HuggingFacePipeline
        
        print("📦 Loading local model...")
        
        # Create a text generation pipeline
        pipe = pipeline(
            "text-generation",
            model="microsoft/DialoGPT-small",
            max_new_tokens=128,
            temperature=0.1,
            device=-1,  # Use CPU
            return_full_text=False
        )
        
        llm = HuggingFacePipeline(pipeline=pipe)
        
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=2
        )
        
        return agent
        
    except ImportError:
        print("❌ transformers not installed. Install with: pip install transformers torch")
        return None
    except Exception as e:
        print(f"❌ Local agent creation failed: {e}")
        return None

# 🚀 Main execution function
def main():
    
    query = (
        "Investigate any suspicious events involving buses or crowds near the Garage. "
        "Use alerts, detection logs, and visual captions."
    )
    
    # Strategy 1: Manual execution (most reliable)
    print("🎯 STRATEGY 1: Manual Tool Execution")
    print("="*50)
    try:
        results = execute_manual_workflow()
        print(f"\n✅ Manual workflow completed successfully!")
        return results
    except Exception as e:
        print(f"❌ Manual workflow failed: {e}")
    
    # Strategy 2: Simple agent
    print("\n🎯 STRATEGY 2: Simple LangChain Agent")
    print("="*50)
    try:
        agent = create_simple_agent()
        if agent:
            print("✅ Agent created successfully!")
            response = agent.invoke({"input": query})
            print(f"\n🧠 Agent Response: {response}")
            return response
    except Exception as e:
        print(f"❌ Simple agent failed: {e}")
    
    # Strategy 3: Alternative model
    print("\n🎯 STRATEGY 3: Alternative Model Agent")
    print("="*50)
    try:
        agent = create_alternative_agent()
        if agent:
            print("✅ Alternative agent created!")
            response = agent.invoke({"input": query})
            print(f"\n🧠 Agent Response: {response}")
            return response
    except Exception as e:
        print(f"❌ Alternative agent failed: {e}")
    
    # Strategy 4: Local pipeline
    print("\n🎯 STRATEGY 4: Local Pipeline Agent")
    print("="*50)
    try:
        agent = create_local_agent()
        if agent:
            print("✅ Local agent created!")
            response = agent.invoke({"input": query})
            print(f"\n🧠 Agent Response: {response}")
            return response
    except Exception as e:
        print(f"❌ Local agent failed: {e}")
    
    print("\n❌ All strategies failed!")
    print("💡 Check that your tools are properly implemented in src/langchain_tools.py")

if __name__ == "__main__":
    main()