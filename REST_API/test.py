import requests


BASE = "http://127.0.0.1:5000/"

def get_video (id) : 
    response = requests.get(BASE + f"Video/{str(id)}").json()
    return response
def add_video (title) :
    response = requests.put(BASE + "Video",json= {"title" : title})
    return response.json()

def update_video (id,title,likes) :
    #only update fields that are not None
    if title is None and likes is None:
        return {"message": "No fields to update"}
    data = {}
    if title is not None:
        data["title"] = title
    if likes is not None:
        data["likes"] = likes
    response = requests.patch(BASE + f"Video/{str(id)}", json=data)    
    return response.json()

def delete_video (id : int) :
    response = requests.delete(BASE + f"Video/{str(id)}")
    return response.json()

def main () : 
    print("1. Add Video")
    print("2. Delete Video")
    print("3. Update Video")
    print("4. Get Video")
    choice = input("Enter your choice: ")
    if choice == "1" :
        title = input("Enter video title: ")
        response = add_video(title)
        print("Response:", response)
    elif choice == "2" :
        id = int(input("Enter video ID to delete: "))
        response = delete_video(id)
        print("Response:", response)
    elif choice == "3" :
        # lets users choose which fields to update
        id = int(input("Enter video ID to update: "))
        title = input("Enter new title (leave blank to keep current): ")
        likes = input("Enter new likes (leave blank to keep current): ")
        response = update_video(id, title if title else None, int(likes) if likes else None)
        print("Updated video:", response)

    elif choice == "4" :
        id = int(input("Enter video ID to get: "))
        response = get_video(id)
        print("Video details:", response)
    else :
        print("Invalid choice")

if __name__ == "__main__" :
    main()        

