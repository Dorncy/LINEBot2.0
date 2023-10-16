import firebase_admin
from firebase_admin import credentials, firestore
import random
from chatGPT import reply_stablemsg

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def get_all_view(area):
    db = firestore.client()

    collection_ref = db.collection(area)
    docs = collection_ref.get()

    info = ""
    for doc in docs:
        result = doc.to_dict()
        info += result.get("view") + "\n"
    return info


def get_view_introducion(view, area):
    db = firestore.client()

    # collection_names = [
    #     "台中", "苗栗", "彰化", "南投", "雲林", "台北", "新北", "基隆",
    #     "桃園", "新竹", "宜蘭", "高雄", "台南", "嘉義", "屏東", "花蓮", "台東"]
    # info = ""
    # for collection_name in collection_names:
    #     collection_ref = db.collection(collection_name)
    #     docs = collection_ref.where('view', '==', view)
    #     results = docs.get()
    #     for doc in results:
    #         result = doc.to_dict()
    #         info += "景點：" + result.get("view") + "\n"
    #         info += "景點介紹：" + result.get("introduction") + "\n"
    #         info += "地址：" + result.get("address")
    #         # info += "開放時間：" + result.get("time") + "\n\n"
    #         # info += "票價：" + result.get("ticket")
    # # print(info)
    info = ""
    collection_ref = db.collection(area)
    docs = collection_ref.where('view', '==', view)
    results = docs.get()
    for doc in results:
        result = doc.to_dict()
        info += "景點：" + result.get("view") + "\n"
        info += "景點介紹：" + result.get("introduction") + "\n"
        info += "地址：" + result.get("address")

    return info


# get_view_introducion("高美濕地")


def random_view_introduction(area):
    db = firestore.client()

    collection_ref = db.collection(area)
    docs = collection_ref.get()

    place_id = []

    num = random.randint(0, len(docs)-1)
    place_id.append(docs[num])

    place = ''
    for doc in place_id:
        result = doc.to_dict()
        place += result.get('view')

    info = get_view_introducion(place, area)

    return info


# print(reply_stablemsg(random_view_introduction('台中')))
# print(random_view_introduction('台中'))
