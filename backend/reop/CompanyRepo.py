from backend.entity.Company import Company


class CompanyRepo:
    def __init__(self, session):
        self.session = session

    def _merge(self, resume: dict):
        with self.session() as session, session.begin():
            session.merge(Company(**resume))

    def merge(self, resume: dict):
        self._merge(resume)

    def search_by_condition(self, column_dict: dict):
        print('column_dict',column_dict)
        with self.session() as session, session.begin():
            found_list = []
            found_row = session.query(Company).filter_by(**column_dict).all()
            for each_row in found_row:
                found_list.append(each_row.to_dict())
            print('fond_list',found_list)
            
            return found_list

    def del_by_condition(self, column_dict: dict):
        with self.session() as session, session.begin():
            session.query(Company).filter_by(**column_dict).delete()