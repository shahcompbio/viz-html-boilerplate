# Boilerplate (HTML)

This project is a boilerplate for standalone HTML dashboards, using a Jinja template. This required both yarn and python3.

It was bootstrapped with Create React App

## How to use

To use the boilerplate:

```
git clone --depth=1 https://github.com/shahcompbio/viz-html-boilerplate.git <your project name>
rm -r <your project name>/.git
```

Remember to change:

- Project name in package.json

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `yarn build`

This will bundle React in production mode to the `build` folder, creating a data-less Jinja template.

To bundle into a single HTML, run `python build_template.py` file to merge all JS and CSS files into `dist/template.html`
