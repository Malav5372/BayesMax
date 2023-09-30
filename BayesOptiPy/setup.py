from setuptools import setup, find_packages


setup(
    name='Bayes-Max',
    version="1.4.3",
    url='https://github.com/Malav5372/BayesMax',
    packages=find_packages(),
    author='Malav Patel',
    author_email="malavpatel038@gmail.com",
    description='Bayesian Optimization package',
    long_description="A Python implementation of global optimization with gaussian processes.",
    python_requires='>= 3.7',
    install_requires=[
        "numpy >= 1.9.0",
        "scipy >= 1.0.0",
        "scikit-learn >= 0.18.0",
        "colorama >= 0.4.6"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ]
)
