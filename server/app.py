from openenv.core.env_server import create_fastapi_app
from env.env import EmailEnvironment
from env.models import EmailAction, EmailObservation


def create_app():
    return create_fastapi_app(
        EmailEnvironment,
        action_cls=EmailAction,
        observation_cls=EmailObservation
    )


app = create_app()


# VALIDATION
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()