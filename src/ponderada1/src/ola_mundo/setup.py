from setuptools import find_packages, setup

package_name = 'ola_mundo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabriela',
    maintainer_email='gabriela.matias@sou.inteli.edu.br',
    description='TODO: Package description',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ola=ola_mundo.ola:main",
        ],
    },
)
