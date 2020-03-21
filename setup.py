from setuptools import setup

package_name = 'fastrtpsgen_scripts'

setup(
    name=package_name,
    version='0.0.0',
    data_files=[(f'share/{package_name}/hook', ['resources/hook.sh'])],
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='James Pace',
    maintainer_email='jpace121@gmail.com',
    description='Python wrapper to call fastrtpsgen.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': ['fasrtpsgen=fastrtpsgen_scripts.fastrtpsgen:main'],
    },
)
