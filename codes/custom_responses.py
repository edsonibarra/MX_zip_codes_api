def create_zip_code_not_found_response(zip_code):
    return {
        "zip_code": zip_code,
        "message": f"{zip_code} does not exists or it couldn't be found on our database"
    }


def create_zip_code_response(results):
    return {
        "zip_code": results["d_codigo"],
        "locality": results["d_ciudad"].upper(),
        "federal_entity": {
            "key": results["c_estado"],
            "name": results["d_estado"].upper(),
            "code": results["c_CP"] if results["c_CP"] else None
        },
        "settlements": [],
        "municipality": {
            "key": results["c_mnpio"],
            "name": results["D_mnpio"]
        } 
    }