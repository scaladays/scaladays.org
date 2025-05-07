# ScalaDays Website

This repository contains the source code for the ScalaDays website. The website is built using [Jekyll](https://jekyllrb.com/) and [Bootstrap](https://getbootstrap.com/docs/5.0).

## Project Structure

### Key Directories and Files

- `_config.yml`: Main configuration file for the Jekyll site.
- `_data/`: Contains YAML files with data used in the site.
- `_includes/`: Contains HTML partials that can be included in other templates.
- `_layouts/`: Contains layout templates for the site.
- `_posts/`: Contains blog posts.
- `_talks-2025/`: Contains the different talks.
- `_workshops/`: Contains the workshops content.
- `_sass/`: Contains SCSS files for styling.
- `css/`: The basic import for the stylings.
- `js/`: Some JS code. Currently used for the navbar transparency on scrolling and the countdown logic.
- `img/`: Images and assets used for the page, the talks and blog posts.
- `_site/`: Output directory for the generated site (ignored by Git).
- `.github/`: Contains GitHub Actions workflows for CI/CD.
- `Gemfile`: Specifies the Ruby gems required for the project.
- `index.md`: The main landing page for the site.
- `README.md`: This file.

Besides the main index, there are some other basic paths in the site:

- `/schedule` (`/schedule.html`)
- `/2025/[item]` (`/_layouts/schedule-detail.html`)
- `/speakers` (`/speakers.md`)
- `/sponsorhips` (`/the-sponsor.html`)
- `/the-venue` (`/the-venue.html`)
- `/blog` (`/blog.html`)
- `/blog/[item]` (`/_layouts/post-detail.html`)
- `/workshops` (`/workshops-list.html`)
- `/workshops/[item]` (`/_layouts/workshops-detail.html`)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ScalaDays.git
   cd ScalaDays
	 ```

2. Install the required gems:
   ```sh
   bundle install
   ```

## Development

To start the Jekyll development server, run:
```sh
bundle exec jekyll serve
```
This will start a local server at `http://localhost:4000` where you can view the site.

Or, depending on your configuration settings, you should use:

```sh
bundle exec jekyll serve --baseurl "/ScalaDays"
```

That will start the local server at `http://localhost:4000/ScalaDays`. mimicking the default deployemnt configuration using ScalaDays as `baseurl` parameter.


## Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions. The workflow is defined in `build-and-deploy.yml`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
