from runners.python import Submission
import re


class MathieuSubmission(Submission):
    def re_position(self, line):
        position = re.search(r'p=<(-?\d+),(-?\d+),(-?\d+)>', line)
        return tuple(int(pos) for pos in position.group(1, 2, 3))

    def re_velocity(self, line):
        velocity = re.search(r'v=<(-?\d+),(-?\d+),(-?\d+)>', line)
        return tuple(int(vel) for vel in velocity.group(1, 2, 3))

    def re_acceleration(self, line):
        acceleration = re.search(r'a=<(-?\d+),(-?\d+),(-?\d+)>', line)
        return tuple(int(acc) for acc in acceleration.group(1, 2, 3))

    def run(self, s):
        positions_t = [self.re_position(line) for line in s.split('\n')]
        velocities_t = [self.re_velocity(line) for line in s.split('\n')]
        accelerations = [self.re_acceleration(line) for line in s.split('\n')]
        n = s.count('\n') + 1
        remaining_particles = set(range(n))
        collisions = self.particles_in_collision(positions_t, remaining_particles)
        remaining_particles = remaining_particles - collisions
        while not self.no_more_collision(remaining_particles,positions_t,accelerations):
            for particle in remaining_particles:
                velocities_t[particle]=tuple(map(sum,zip(velocities_t[particle],accelerations[particle])))
                positions_t[particle]=tuple(map(sum, zip(positions_t[particle],velocities_t[particle])))
            collisions = self.particles_in_collision(positions_t, remaining_particles)
            remaining_particles = remaining_particles - collisions

        return len(remaining_particles)

    def no_more_collision(self, remaining_particles, positions_t, accelerations):
        projection_x = [(positions_t[particle][0], accelerations[particle][0]) for particle in remaining_particles]
        projection_x = sorted(projection_x, key=lambda x: x[0])
        no_more_collision_x = all(par_0[1] <= par_1[1] for par_0, par_1 in zip(projection_x[:-1], projection_x[1:]))

        projection_y = [(positions_t[particle][1], accelerations[particle][1]) for particle in remaining_particles]
        projection_y = sorted(projection_y, key=lambda x: x[0])
        no_more_collision_y = all(par_0[1] <= par_1[1] for par_0, par_1 in zip(projection_y[:-1], projection_y[1:]))

        projection_z = [(positions_t[particle][2], accelerations[particle][2]) for particle in remaining_particles]
        projection_z = sorted(projection_z, key=lambda x: x[0])
        no_more_collision_z = all(par_0[1] <= par_1[1] for par_0, par_1 in zip(projection_z[:-1], projection_z[1:]))

        return no_more_collision_x and no_more_collision_y and no_more_collision_z

    def particles_in_collision(self, positions_t, remaining_particles):
        if len(remaining_particles)==len(set(positions_t[part] for part in remaining_particles)):
            return set()
        else:
            collision = set()
            to_visit = set(remaining_particles)
            to_remove=set()
            while to_visit:
                particule_0 = to_visit.pop()
                to_visit=to_visit-to_remove
                to_remove=set()
                for particule_1 in to_visit:
                    if positions_t[particule_1] == positions_t[particule_0]:
                        collision.add(particule_0)
                        collision.add(particule_1)
                        to_remove.add(particule_1)
            return collision

