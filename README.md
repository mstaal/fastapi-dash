# Dashboards


The purpose of this project is to provide a means of generating dashboards. At the time of this writing, the following types of dashboards are supported:
1. [Plotly Dash](https://plotly.com/dash/)


## Running the project locally
In order to run the project locally, one has to make a copy of `config/local.env.dist` called `config/local.env`
and fill in the relevant secrets. From here, one can run the project either using a local virtual environment
or by running it inside a Docker container.

#### 0. Preliminary: VSCode launch configs
Enter the relevant configs in your `.vscode/launch.json` and `.vscode/settings.json` files. There are examples to bootstrap in the `.vscode` folder.


#### 1. Launch using VSCode 'Run and Debug' tool
First, remember to run the `make poetry_setup` target. After having completed this step, you should be able to run the project
by running the `Dashboards: FastAPI` launcher that you gathered from the previous step.

#### 2. Launch using Docker container
As an alternative, one can launch the project using the `make compose-up` target, which is available in the Makefile.


## Regarding adding a new Dash based dashboard (WIP)
The process around adding a new dashboard i still in the making, but the basic approach for now is as follows:
1. Inside `app/server/dashboards` add a new folder with the name of your dashboard. You may as a starting point bootstrap from the `hello_world` example.
2. Give your dashboard its own name and implement it using the Dash syntax and features.
3. Add your Dash dashboard in the `app/server/dashboards/mounts.py` file.
4. Commit and push your code changes.


## Dashboard URLs
1. **Default local version**: http://localhost:20409
