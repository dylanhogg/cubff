# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from bin import cubff

# struct SimulationState {
#   std::vector<uint8_t> soup;
#   std::vector<uint32_t> shuffle_idx;
#   std::array<std::array<uint8_t, 3>, 256> byte_colors;
#   float elapsed_s;
#   size_t total_ops;
#   float mops_s;
#   size_t epoch;
#   float ops_per_run;
#   size_t brotli_size;
#   float brotli_bpb;
#   float bytes_per_prog;
#   float h0;
#   float higher_entropy;
#   std::array<std::pair<std::string, float>, 16> frequent_bytes;
#   std::array<std::pair<std::string, float>, 16> uncommon_bytes;
#   std::function<void(size_t)> print_program;
# };

def callback(state):
    # state_params = [s for s in dir(state) if not s.startswith('_')]  # state_params=['brotli_bpb', 'brotli_size', 'bytes_per_prog', 'elapsed_s', 'epoch', 'frequent_bytes', 'h0', 'higher_entropy', 'mops_s', 'ops_per_run', 'print_program', 'shuffle_idx', 'soup', 'total_ops', 'uncommon_bytes']
    # print(f"{state_params=}")
    print(f"epoch={state.epoch}, brotli_bpb={state.brotli_bpb}, brotli_size={state.brotli_size}, ops_per_run={state.ops_per_run}, "
          f"higher_entropy={state.higher_entropy}, bytes_per_prog={state.bytes_per_prog}, "
          f"elapsed_s={state.elapsed_s}, total_ops={state.total_ops}, mops_s={state.mops_s}, higher_entropy={state.higher_entropy}, h0={state.h0}")
    state.print_program(1)
    print("")
    return state.epoch > 1024

# struct SimulationParams {
#   size_t num_programs = 128 * 1024;
#   size_t seed = 0;
#   uint32_t mutation_prob = 1 << 18;  // denominator 1<<30.
#   std::optional<size_t> reset_interval = std::nullopt;
#   std::optional<std::string> load_from = std::nullopt;
#   std::optional<std::string> save_to = std::nullopt;
#   size_t callback_interval = 128;
#   size_t save_interval = 0;
#   bool permute_programs = true;
#   bool fixed_shuffle = false;
#   bool zero_init = false;
#   std::vector<std::vector<uint32_t>> allowed_interactions;
# };

params = cubff.SimulationParams()
params.num_programs = 128*1024
params.seed = 0

cubff.RunSimulation("bff_noheads", params, None, callback)
