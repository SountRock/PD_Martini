# Cамосборка липидного бислоя, визуализация и результаты

Выполнено моделирование самосборки липидного бислоя (из случайной стартовой конфигурации) с использованием coarse-grained подхода Martini и расчётами в GROMACS. Для визуализации реализованы два PyMOL-скрипта, генерирующие кадровую анимацию и итоговые GIF-файлы.

## Результаты проекта 
- Полный пайплайн моделирования самосборки бислоя: подготовка -> minim -> NVT -> NPT -> продукционный MD.  
- Скрипты подготовки системы и mdp-шаблоны для последовательных этапов.  
- Анализ траектории: RMSD, RMSF, density(z), area per lipid, order parameters (S_cd), RDF, кластеризация.  
- Автоматизированная визуализация: `render.py`, `render2.py` → PNG кадры → GIF (`trajectory.gif`, `trajectory2.gif`).  
- Итоговый отчёт и набор файлов для воспроизводимости (версии, seed'ы, docker image id).

## Как воспроизвести моделирование (инструкция установки инструментов)
> Установлен Docker; для GPU — настроен `nvidia-container-toolkit`. Инструкция:
```bash
sudo apt update
sudo apt  install docker.io  curl
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo systemctl restart docker
```
> Альтернативно можно запускать нативно при наличии GROMACS с поддержкой MPI/GPU.
> Использовать удобный образ: https://hub.docker.com/r/fbettio/gromacs-plumed-cuda

