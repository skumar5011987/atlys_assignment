from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    proxy: str = ""
    page_limit: int = 5
    cookies: dict = {
        "pys_session_limit":True,
        "pys_start_session":True,
        "pys_first_visit":True,
        "sbjs_migrations":"1418474375998%3D1",
        "sbjs_current_add":"fd%3D2024-07-20%2011%3A04%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fdentalstall.com%2Fshop%2F%7C%7C%7Crf%3D%28none%29",
        "sbjs_first_add":"fd%3D2024-07-20%2011%3A04%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fdentalstall.com%2Fshop%2F%7C%7C%7Crf%3D%28none%29",
        "sbjs_current":"typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29",
        "sbjs_first":"typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29",
        "sbjs_udata":"vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36",
        "_gcl_au":"1.1.2136265836.1721475289",
        "_fbp":"fb.1.1721475289633.647489888899214401",
        "_gid":"GA1.2.411335519.1721475292", 
        "_hjSession_3772814":"eyJpZCI6IjQ1MzJlMDllLTEzMjAtNDQxOS04MmEyLTczMjJmMjkxNTg2MSIsImMiOjE3MjE0NzUyOTIwMTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0:",
        "_clck":"8amn2l%7C2%7Cfnm%7C0%7C1662",
        "_hjSessionUser_3772814":"eyJpZCI6Ijk4NmU3MGRjLWZkNTUtNTY0Yy04NWJlLTMzNjJkMmU5NzEyOCIsImNyZWF0ZWQiOjE3MjE0NzUyOTIwMTYsImV4aXN0aW5nIjp0cnVlfQ::",
        "woo_notification_close":"1",
        "_ga_C5ZBR8L9YD":"GS1.1.1721475288.1.1.1721475854.0.0.0",
        "_ga":"GA1.2.381574688.1721475289", 
        "sbjs_session":"pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdentalstall.com%2Fshop%2F"
    }

settings = Settings()
