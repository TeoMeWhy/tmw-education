# %%
import argparse
import pandas as pd

class CourseImporter:
    def __init__(self, sheet_id:str, gids:dict):
        self.base_URL = "https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid={gid}&format=csv"
        self.sheet_id = sheet_id
        self.gids = gids

    def get_data(self, gid):
        url = self.base_URL.format(sheet_id=self.sheet_id, gid=gid)
        df = pd.read_csv(url)
        return df
    
    def get_all(self):
        dfs = {}
        for i in self.gids:
            dfs[i] = self.get_data(self.gids[i])
        return dfs
    
    def save_all(self, dfs):
        for i in dfs:
            dfs[i].to_csv(f"{i}.csv", sep=";", index=False)

    def process(self):
        dfs = self.get_all()
        self.save_all(dfs)


class SkillImporter:
    
    def __init__(self, sheet_id:str, gids:dict):
        self.base_URL = "https://docs.google.com/spreadsheets/d/{sheet_id}/export?gid={gid}&format=csv"
        self.sheet_id = sheet_id
        self.gids = gids


    def get_bd_skills(self):
        url = self.base_URL.format(sheet_id=self.sheet_id, gid=self.gids["skills"])
        df = pd.read_csv(url)
        df.columns = ['skill', 'descricao']
        df.to_csv("skills.csv", sep=";", index=False)
    

    def get_role_skills(self, role:str):
        url = self.base_URL.format(sheet_id=self.sheet_id, gid=self.gids["roles"][role])
        df = pd.read_csv(url, skiprows=1)
        df = (df.dropna(how="any", axis=0)
                .drop("Descrição", axis=1) 
                .set_index("Skill")
                .stack()
                .reset_index())

        df.columns = ["skill", "role_level", "level"]
        df["role"] = role
        return df
    
    def get_all_roles_skills(self):
        dfs = [self.get_role_skills(i) for i in self.gids["roles"]]
        df = pd.concat(dfs, ignore_index=True, axis=0)
        df = df[["role", "role_level", "skill", "level"]]
        df.to_csv("role_skills.csv", index=False, sep=";")



def extract_skills():
    sheet_id = "1RpGhP2MDjTiyc7TgnrTHCLKMigEvn2x_tGJw8HDkj24"

    gids = {
        "skills": 1223057358,
        "roles":{
            "Data Analyst":   0,
            "Data Engineer":  766909586,
            "Data Scientist": 2098008799,
        }
    }

    skill_importer = SkillImporter(sheet_id=sheet_id, gids=gids)
    skill_importer.get_bd_skills()
    skill_importer.get_all_roles_skills()


def extract_courses():
    sheet_id_courses = "1Dc8LF5GWBd7VEbTB9wLxK5h12z_7s7VbDSKYdjgxuUE"
    gids_courses = {
        "courses":0,
        "courses_eps":1927140059,
    }

    course_importer = CourseImporter(sheet_id=sheet_id_courses, gids=gids_courses)
    course_importer.process()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--skills","-s", action='store_true')
    parser.add_argument("--courses","-c", action='store_true')
    args = parser.parse_args()

    if args.skills:
        extract_skills()

    if args.courses:
        extract_courses()
