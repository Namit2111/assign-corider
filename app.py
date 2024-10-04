from app import create_app
import debugpy

debugpy.listen(("0.0.0.0", 5678))
# print("⏳ Waiting for debugger attach...")
debugpy.wait_for_client()
# print("🎉 Debugger attached")

app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
