import setuptools

with open("README.md", "r") as rd:
    long_description = rd.read()

setuptools.setup(
    name="visionlib",
    version="1.3.0",
    author="Ashwin Vinod",
    author_email="ashwinvinodsa@gmail.com",
    url='https://github.com/ashwinvin/Visionlib',
    download_url='https://github.com/ashwinvin/Visionlib/archive/v1.3.0.tar.gz',
    description="A simple, easy to use and customizeble cv library ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['Deep learning', 'Vision', 'cv'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['mtcnn', 'opencv-python', ' dlib', 'wget', 'numpy'],
    python_requires=">=3.6",
)
