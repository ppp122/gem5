#ifndef __LEARNING_GEM5_JIAJIA_OBJECT_HH__
#define __LEARNING_GEM5_JIAJIA_OBJECT_HH__

#include "params/JiajiaObject.hh"
#include "sim/sim_object.hh"

namespace gem5
{

class JiajiaObject : public SimObject
{
  public:
    JiajiaObject(const JiajiaObjectParams &p);
};

} // namespace gem5

#endif // __LEARNING_GEM5_JIAJIA_OBJECT_HH__
