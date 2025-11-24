"""
Test script to verify the API is working
"""

import requests
import json

# API base URL
API_URL = "http://localhost:8000"

# Sample transcript
SAMPLE_TRANSCRIPT = """
Hello everyone! My name is Sarah Johnson. I am 15 years old and I study at 
Lincoln High School in grade 10. I live with my parents and my younger brother. 
I love reading books, especially mystery novels, and I enjoy playing basketball 
on weekends. I'm also interested in learning new languages. Thank you for 
listening to my introduction!
"""

def test_health_check():
    """Test health check endpoint"""
    print("Testing health check endpoint...")
    try:
        response = requests.get(f"{API_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_evaluate():
    """Test evaluation endpoint"""
    print("\nTesting evaluation endpoint...")
    try:
        payload = {"transcript": SAMPLE_TRANSCRIPT}
        response = requests.post(
            f"{API_URL}/api/evaluate",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\nOverall Score: {result['overall_score']}")
            print(f"Grade: {result['grade']}")
            print(f"Word Count: {result['word_count']}")
            print(f"Sentence Count: {result['sentence_count']}")
            print(f"\nSummary: {result['summary']}")
            print(f"\nCriteria Scores:")
            for criterion in result['criteria_scores']:
                print(f"  - {criterion['criterion']}: {criterion['score']}/{criterion['max_score']} ({criterion['percentage']:.1f}%)")
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("AI Speech Evaluation System - API Test")
    print("=" * 60)
    
    # Test health check
    health_ok = test_health_check()
    
    if health_ok:
        # Test evaluation
        eval_ok = test_evaluate()
        
        if eval_ok:
            print("\n" + "=" * 60)
            print("✅ All tests passed!")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("❌ Evaluation test failed")
            print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ Health check failed - is the server running?")
        print("=" * 60)
