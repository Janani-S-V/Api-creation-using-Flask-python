from flask import Flask
from fastapi import FastAPI, HTTPException
app = FastAPI()
dic = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}
@app.post("/create/{key}/{value}")
def create_entry(key: str, value: str):
    dic[key] = value
    return {"message": "Entry created successfully"}
@app.get("/read/{key}")
def read_entry(key: str):
    if key in dic:
        return {"key": key, "value": dic[key]}
    else:
        return {"message": f"Key '{key}' not found"}
@app.put("/update/{key}/{value}")
def update_entry(key: str, value: str):
    if key in dic:
        dic[key] = value
        return {"message": "Entry updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Key not found")
@app.delete("/delete/{key}")
def delete_entry(key: str):
    if key in dic:
        del dic[key]
        return {"message": "Entry deleted successfully"}
    else:
        return {"message": f"Key '{key}' not found"}
if __name__ == '__main__':
    app.run(debug=True)  