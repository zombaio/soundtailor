/// @file firstorder_polezero.h
/// @brief Low Pass using a simple 1st order pole-zero filter
/// @author gm
/// @copyright gm 2014
///
/// This file is part of SoundTailor
///
/// SoundTailor is free software: you can redistribute it and/or modify
/// it under the terms of the GNU General Public License as published by
/// the Free Software Foundation, either version 3 of the License, or
/// (at your option) any later version.
///
/// SoundTailor is distributed in the hope that it will be useful,
/// but WITHOUT ANY WARRANTY; without even the implied warranty of
/// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
/// GNU General Public License for more details.
///
/// You should have received a copy of the GNU General Public License
/// along with SoundTailor.  If not, see <http://www.gnu.org/licenses/>.

#ifndef SOUNDTAILOR_SRC_FILTERS_FIRSTORDER_POLEZERO_H_
#define SOUNDTAILOR_SRC_FILTERS_FIRSTORDER_POLEZERO_H_

#include "soundtailor/src/common.h"
#include "soundtailor/src/filters/filter_base.h"

namespace soundtailor {
namespace filters {

/// @brief Chamberlin state variable low pass filter
class FirstOrderPoleZero : public Filter_Base {
 public:
  FirstOrderPoleZero();
  virtual ~FirstOrderPoleZero() {
    // Nothing to do here for now
  }
  virtual Sample operator()(SampleRead sample);
  virtual void SetParameters(const float frequency, const float resonance);

 protected:
  double coeff_;
  float last_input_;
  float last_output_;
};

}  // namespace filters
}  // namespace soundtailor

#endif  // SOUNDTAILOR_SRC_FILTERS_FIRSTORDER_POLEZERO_H_